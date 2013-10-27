import os, sys
os.environ['PYTHONINSPECT'] = 'True'

def findRightBoundary(buildings):
	"""
	To find the rightmost boundary of all buildings
	O(n)
	"""
	return max([y[2] for y in buildings]) + 1

def draw(buildings):
	"""
	Use heights to represent the horizontal axis
	O(n^2)
	"""
	heights = [0] * findRightBoundary(buildings)
	for b in buildings:
		for i in range(b[0], b[2]):
			if b[1] > heights[i]:
				heights[i] = b[1]
	return heights

def convert(heights):
	"""
	Convert heights to the correct output format
	Odd element: X-axis index
	Even element: Y-axis index
	"""
	skyline = []
	skyline.append(0)
	skyline.append(heights[0])

	for i in range(1, len(heights)):
		if heights[i] != heights[i - 1]:
			skyline.append(i)
			skyline.append(heights[i])
	return skyline


if __name__ == '__main__':
	buildings = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29), (24,4,28)]
	heights = draw(buildings)
	skyline = convert(heights)
	print skyline
