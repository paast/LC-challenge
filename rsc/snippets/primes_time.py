import time

def f():
	for num in range(1000000):
		x = num * num

start = time.time_ns()
f()
elapsed = time.time_ns() - start

# prints ~50000000 for me (0.05 seconds)
print(elapsed)