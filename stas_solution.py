import math
# левое уравнение координаты х и у
def first_equation(array):
	x_1 = []
	y = 1
	summa = 1
	for x in range(len(array)):
		x_1.append(1/(array[x] - y + 1))
		y = y + 1
		print(" кординаты левого уравнения  x = " + str(array[x]) + " y = " + str(x_1[x]))
	print("сумма  = " + str(sum(x_1)))
	
# правое уравнение координаты х и у
def two_equation(array,array_1):
	x_1 = []
	for x in range(len(array)):
		x_1.append((26*array_1[x])/(array[x] + 1)* array_1[x] - (x * array_1[x]))
		print("координаты правого уравнения  x = " + str(array[x]) + " y = " + str(x_1[x]))
# отделяем корни уравнения
def three_equation(array, array_1):
	x_1 = []
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
			print ("корень на отрезке " + str(array[root]) + " " + str(array[count]))
		count += 1	
def findTheDerivativeOfTheFirstPoint():
	result = 25/(30-3)**2
	return result

def findTheDerivativeOfTheTwoPoint():
	result = 25/(31-3)**2
	return result

def findRoot(result,result_1):
	#root = []
	error = 0.001
	c = -(1/result)
	#for x in range(0,20):
	root = 30.5 + c *(1/ 30.5 - 4 + 1) - (26 * 7/(30.5 + 1)*7 - (4 * 7))
	return root


def main():
	array_1 = [9, 12, 11, 4, 7, 2, 5, 8, 5, 7, 1, 6, 1, 9, 4, 1, 3, 3, 6, 1, 11, 33,
	7, 91, 2, 1]
	array = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38, 40, 45, 50, 54, 69, 100, 1010, 2000, 2010,10000, 10001, 99900,
	99990, 99991,  100000]
	# first_equation(array)
	# two_equation(array,array_1)
	#three_equation(array, array_1)
	result = findTheDerivativeOfTheFirstPoint()
	print(result)
	result_1 = findTheDerivativeOfTheTwoPoint()
	print(result_1)
	root = findRoot(result,result_1)
	print(root)
