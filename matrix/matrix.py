
def printMatrix(matrix):
	if matrix is None:
		print("None")
		return
	for r in matrix:
		for x in r:
			print(str(x).rjust(6), end = "")
		print()

def transpose(matrix):
	r_count, c_count = len(matrix), len(matrix[0])
	res = []
	for c in range(c_count):
		res.append([matrix[r][c] for r in range(r_count)])
	return res

def addSub(m_one, m_two, sw):
	m_one_size = (len(m_one[0]), len(m_one))
	m_two_size = (len(m_two[0]), len(m_two))
	if m_one_size != m_two_size:
		return

	res = []
	for r_one, r_two in zip(m_one, m_two):
		res.append([x + sw * y for x, y in zip(r_one, r_two)])
	return res

def add(m_one, m_two):
	return addSub(m_one, m_two, 1)

def subtract(m_one, m_two):
	return addSub(m_one, m_two, -1)

def multiply(m_one, m_two):
	m_one_dim = (len(m_one[0]), len(m_one))
	m_two_dim = (len(m_two[0]), len(m_two))
	res_dim = (m_one_dim[1], m_two_dim[0])
	if m_one_dim[0] != m_two_dim[1]:
		return
	res = []
	for r in range(res_dim[0]):
		res.append([])
		for c in range(res_dim[1]):
			value = sum([x * y for x, y in zip(m_one[r], transpose(m_two)[c])])
			res[r].append(value)
	return res


one = [[-3, 3], [4, 1], [-2, -1], [2, 5]]
two = [[0, 3], [4, 1]]
f = multiply(one, two)
printMatrix(f)
