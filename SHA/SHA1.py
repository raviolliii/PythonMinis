
CHAR_SIZE = 8

def uint32(n):
	if isinstance(n, str):
		n = int(n, 2)
	return n & 0xFFFFFFFF

def pad(n, bits):
	bitstring = "{0:0" + str(bits) + "b}"
	return bitstring.format(n)

def chunkify(data, size):
	return [data[i:i + size] for i in range(0, len(data), size)]

def rotateLeft(bits, turns):
	res = bits[turns:] + bits[:turns]
	return res

def preProcess(message):
	bitstring = ""
	for letter in message:
		c = int(ord(letter))
		bitstring += pad(c, 8)
	bitstring += "1"

	while len(bitstring) % 512 != 448:
		bitstring += "0"

	ml = len(message) * CHAR_SIZE
	ml = pad(ml, 8)
	ml = ("0" * (64 - len(ml))) + ml

	return bitstring + ml

def SHA1(message):
	H0 = 0x67452301
	H1 = 0xEFCDAB89
	H2 = 0x98BADCFE
	H3 = 0x10325476
	H4 = 0xC3D2E1F0

	bits = preProcess(message)
	chunks = chunkify(bits, 512)

	for i in range(len(chunks)):
		chunk = chunks[i]
		words = chunkify(chunk, 32)

		for j in range(16, 80):
			wordVals = [words[j - 3], words[j - 8], words[j - 14], words[j - 16]]
			uint32Vals = list(map(lambda n: uint32(n), wordVals))
			# could use reduce here, but have to import functools and i'm already this deep
			xorTotal = 0
			for val in uint32Vals:
				xorTotal ^= val
			paddedBin = pad(uint32(xorTotal), 32)
			words.append(rotateLeft(paddedBin, 1))

		a, b, c, d, e = H0, H1, H2, H3, H4

		for j in range(80):
			f, k = 0, 0
			if j < 20:
				f = (b & c) | (~b & d)
				k = 0x5A827999
			elif j < 40:
				f = b ^ c ^ d
				k = 0x6ED9EBA1
			elif j < 60:
				f = (b & c) | (b & d) | (c & d)
				k = 0x8F1BBCDC
			else:
				f = b ^ c ^ d
				k = 0xCA62C1D6

			f = uint32(f)

			aRot = rotateLeft(pad(a, 32), 5)
			aInt = uint32(aRot)
			wordInt = uint32(words[j])
			t = aInt + f + e + k + wordInt
			e = uint32(d)
			d = uint32(c)
			bRot = rotateLeft(pad(b, 32), 30)
			c = uint32(bRot)
			b = uint32(a)
			a = uint32(t)

		H0 = uint32(H0 + a)
		H1 = uint32(H1 + b)
		H2 = uint32(H2 + c)
		H3 = uint32(H3 + d)
		H4 = uint32(H4 + e)

	HH = list(map(lambda H: hex(H)[2:].rjust(8, "0"), [H0, H1, H2, H3, H4]))
	return "".join(HH)

