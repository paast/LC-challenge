import timeit

def f(x):
	return x * x

print(timeit.timeit("f(6)", setup="from __main__ import f", number=1000000))