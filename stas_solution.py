import math
from max_number import maximum1, average
from findRoot import findCoefficient
from parser import get_data
# нахождения отрезка на кординатной прямой, где лежит корень  
def three_equation(array,array_1):
	x_1 = []
	point = []
	y = 1
	res = 0
	count = 1
	for x in range(len(array)):
		x_1.append(1/(array[x] - y + 1) - ((26*array_1[x])/(array[x] + 1)* array_1[x] - (x * array_1[x])))
		y = y + 1
		#print("F(b) = F(b) - F(b_1) =   x = " + str(array[x]) + " y = " + str(x_1[x]))
	for root in range(0,25):
		res = x_1[root] + x_1[count]
		if x_1[root] < 0 and x_1[count] > 0:
			point.append(array[root])
			point.append(array[count])
			return point
		count += 1
	else:
		return "roots no!!"	
# сумма производных первого точки
def findTheDerivativeOfTheFirstPoint():
	count = 1
	result = 0
	for x in range(len(array_1)):
		result += (-1/(30 - count + 1))**2 -(-26 * array_1[x])/((array_1[x] *30 + array_1[x]) - (array_1[x] * count))**2
		count += 1
	return result
# сумма производных второго точки
def findTheDerivativeOfTheTwoPoint():
	count = 1
	result = 0
	for x in range(len(array_1)):
		result += (-1/(31 - count + 1))**2 - (-26 * array_1[x])/((array_1[x] *31 + array_1[x]) - (array_1[x] * count))**2
		count += 1
	return result
# нахождения приближёного корня 
def findAppoximateRootValue():
	average_ = average(array, array_1)
	count = 1
	root = 0
	coefficient = findCoefficient()
	for x in range(len(array_1)):
		root = average_ + coefficient *(1/average_ - count + 1) - (26*array_1[x]/((average_ + 1)*array_1[x] - (count * array_1[x])))
		if root > average_ and root < 31:
			return root
		count += 1
	else:
		print("no roots")

# проверка шага 
def checkRoot():
	count = 1
	root = 0
	coefficient = findCoefficient()
	appoximateRootValue = findAppoximateRootValue()
	s = findAppoximateRootValue() - average(array, array_1)
	for x in range(len(array_1)):
		root = appoximateRootValue + coefficient *(1/appoximateRootValue - count + 1) - (26*array_1[x]/((appoximateRootValue + 1)*array_1[x] - (count * array_1[x])))
		if root > appoximateRootValue and root < 31:
			print(root)
			return root
		count += 1
	else:
		print("no more roots")
	

array_1 = ([int(x[1])for x in get_data()])
array = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38, 40, 45, 50, 54, 69, 100, 1010, 2000, 2010,10000, 10001, 99900,
99990, 99991,1000000]

		