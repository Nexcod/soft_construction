import math
import stas_solution as s
def maximum1():
	first = s.findTheDerivativeOfTheFirstPoint()
	two = s.findTheDerivativeOfTheTwoPoint()
	m = math.fabs(max(first,two))
	return m


