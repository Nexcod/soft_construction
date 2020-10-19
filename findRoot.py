import stas_solution as s 
from max_number import *
# нахождения коэффициента
def findCoefficient():
	maxNumber = maximum1()
	firstDerivative = s.findTheDerivativeOfTheFirstPoint()
	if firstDerivative > 0:
		return -1/maxNumber
	else:
		return 1/maxNumber



