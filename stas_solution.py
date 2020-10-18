import math
from max_number import maximum1
from findRoot import findCoefficient
from parser import get_data
def three_equation(array,array_1):
	x_1 = []
	point = []
	y = 1
	res = 0
	count = 1
	for x in range(len(array)):
		x_1.append(1/(array[x] - y + 1) - ((26*array_1[x])/(array[x] + 1)* array_1[x] - (x * array_1[x])))
		y = y + 1
		print("F(b) = F(b) - F(b_1) =   x = " + str(array[x]) + " y = " + str(x_1[x]))
	for root in range(0,25):
		res = x_1[root] + x_1[count]
		if x_1[root] < 0 and x_1[count] > 0:
			point.append(array[root])
			point.append(array[count])
			return point
		count += 1
	else:
		return "roots no!!"	

def findTheDerivativeOfTheFirstPoint():
	count = 1
	result = 0
	for x in range(len(array_1)):
		result += (-1/(30 - count + 1))**2 -(-26 * array_1[x])/((array_1[x] *30 + array_1[x]) - (array_1[x] * count))**2
		count += 1
	return result

def findTheDerivativeOfTheTwoPoint():
	count = 1
	result = 0
	for x in range(len(array_1)):
		result += (-1/(31 - count + 1))**2 - (-26 * array_1[x])/((array_1[x] *31 + array_1[x]) - (array_1[x] * count))**2
		count += 1
	print(result)
	return result

def findAppoximateRootValue():
	count = 1
	root = 0
	k = maximum1()
	coefficient = findCoefficient()
	for x in range(len(array_1)):
		root = 30.5 + coefficient *(1/30.5 - count + 1) - (26*array_1[x]/((30.5 + 1)*array_1[x] - (count * array_1[x])))
		count += 1
		if root > 30.5 and root < 30.95:
			return root
	else:
		print("no root")

array_1 = ([int(x[1])for x in get_data()])
array = [26, 27, 28, 29, 30, 30.5, 31, 32, 33, 34, 35, 38, 40, 45, 50, 54, 69, 100, 1010, 2000, 2010,10000, 10001, 99900,
99990, 99991,]

		