import stas_solution as solution

def findCoefficient():
	firstDerivative = solution.findTheDerivativeOfTheFirstPoint()
	print(firstDerivative)
	if firstDerivative > 0:
		return -1/firstDerivative
	else:
		return 1/firstDerivative

def findRoot():
	root = solution.findAppoximateRootValue()
	print(root)
