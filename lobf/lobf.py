from matplotlib import pyplot as graph

def parseCoords(inpt):
	inpt = inpt.split(", ")
	x = int(inpt[0])
	y = int(inpt[1])
	return (x, y)

def meanX(coords):
	total = 0
	for x, y in coords:
		total += x
	return total / len(coords)

def meanY(coords):
	total = 0
	for x, y in coords:
		total += y
	return total / len(coords)

def calcSlope(coords):
	X = meanX(coords)
	Y = meanY(coords)
	dY, dX = 0, 0
	for x, y in coords:
		dY += (x - X) * (y - Y)
		dX += (x - X) ** 2
	return dY / dX

def calcIntercept(m, X, Y):
	return Y - (m * X)

def calcLine(coords):
	mx = meanX(coords)
	my = meanY(coords)
	m = calcSlope(coords)
	b = calcIntercept(m, mx, my)
	line = (m, b)
	showPlot(coords, line)

def showPlot(coords, line):
	xpoints = [coord[0] for coord in coords]
	ypoints = [coord[1] for coord in coords]
	xlist = range(min(xpoints), max(xpoints) + 1)
	ylist = [(x * line[0]) + line[1] for x in xlist]
	# graph
	graph.grid()
	graph.scatter(xpoints, ypoints, 12, "black")
	graph.plot(xlist, ylist, "red")
	graph.title("Line of Best Fit")
	graph.show()

if __name__ == "__main__":
	file = open("coordinates.txt", "r")
	coords = []
	for line in file:
		coord = parseCoords(line.strip()[1:-1])
		coords.append(coord)

	calcLine(coords)
	print("\nok bye")
