import math
import stas_solution as s
from parser import get_data

def maximum1():
	first = s.findTheDerivativeOfTheFirstPoint()
	two = s.findTheDerivativeOfTheTwoPoint()
	m = math.fabs(max(first,two))
	return m

def average(array,array_1):
	averages = 0
	arrayPoint = s.three_equation(array, array_1)
	averages = (arrayPoint[0] + arrayPoint[1])/2
	return averages
