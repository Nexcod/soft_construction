import math
from max_number import *
# отделяем корни уравнения
def three_equation(array, array_1):
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
#  производная f(a) 
def findTheDerivativeOfTheFirstPoint():
	result = 25/((30-3)**2)
	return result
#  производная f(b)
def findTheDerivativeOfTheTwoPoint():
	result = 25/((31-3)**2)
	return result

def findRoot():
	k = maximum1()
	c = -1/k
	root = 30.5 + c *(1/30.5 - 4 + 1) - (26 * 5/(30.5 + 1)*5 - (4 * 5))
	print(root)
	return root

array_1 = [9, 12, 11, 4, 7, 2, 5, 8, 5, 7, 1, 6, 1, 9, 4, 1, 3, 3, 6, 1, 11, 33,
7, 91, 2, 1]
array = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38, 40, 45, 50, 54, 69, 100, 1010, 2000, 2010,10000, 10001, 99900,
99990, 99991,  100000]


	
	# result = three_equation(array, array_1)
	# print(result)
	#result = findTheDerivativeOfTheFirstPoint()
	# print(result)
	#result_1 = findTheDerivativeOfTheTwoPoint()
	# print(result_1)
	# root = findRoot(result,result_1)
	# print(root)
