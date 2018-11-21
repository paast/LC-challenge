
# OBJECTIVE: create a recursive_fibonacci() function which achieves 
# the same result as the naive one, but using recursion.

import sys


def fib(n):
	if (n < 2): return n
	prev = 1
	cur = 0
	for _ in range(n):
		hold = cur
		cur += prev
		prev = hold
	return cur

def recursive_fib(n):
	if (n < 2): return n
	return recursive_fib(n - 1) + recursive_fib(n - 2)

# golf for lulz
def f(n):return n if(n<2)else f(n-1)+f(n-2)

def g(n):
	return (n if (n < 2) else f(n - 1) + f(n - 2))

def run():
	n = 0
	if (sys.argv[1]):
		n = int(sys.argv[1])

	# naive Fibonacci function
	print(fib(n))

	# recursive Fibonacci function
	print(recursive_fib(n))

	print(f(n))


#~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
	run()
