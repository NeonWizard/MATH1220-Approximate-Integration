import numpy as np

def left_endpoint(n, a, b, function):
	dx = (b-a) / n
	sum = 0
	for xi in np.arange(a, b, dx):
		sum += function(xi)
	return round(sum * dx, 5)

def right_endpoint(n, a, b, function):
	dx = (b-a) / n
	sum = 0
	for xi in np.arange(a+dx, b+dx, dx):
		sum += function(xi)
	return round(sum * dx, 5)

def midpoint(n, a, b, function):
	dx = (b-a) / n
	sum = 0
	for xi in np.arange(a+dx/2, b+dx/2, dx):
		sum += function(xi)
	return round(sum * dx, 5)

def trapezoidal(n, a, b, function):
	dx = (b-a) / n
	sum = function(a) + function(b)
	for xi in np.arange(a+dx, b, dx):
		sum += 2 * function(xi)
	return round(sum * dx/2, 5)

def simpsons(n, a, b, function):
	if n % 2 != 0:
		raise ValueError("N must be even.")

	dx = (b-a) / n
	sum = function(a) + function(b)
	for i, xi in enumerate(np.arange(a+dx, b, dx)):
		if i % 2 == 0:
			sum += 4 * function(xi)
		else:
			sum += 2 * function(xi)
	return round(sum * dx/3, 5)

if __name__ == "__main__":
	assert left_endpoint(5, 0, 2, lambda x: x**2) == 1.92
	assert right_endpoint(5, 0, 2, lambda x: x**2) == 3.52
	assert midpoint(5, 0, 2, lambda x: x**2) == 2.64
	assert trapezoidal(5, 0, 2, lambda x: x**2) == 2.72

	threw_error = False
	try:
		simpsons(5, 0, 2, lambda x: x**2)
	except ValueError:
		threw_error = True
	assert threw_error

	assert simpsons(4, 0, 2, lambda x: x**2) == 2.66667

	print("Tests passed successfully.")
