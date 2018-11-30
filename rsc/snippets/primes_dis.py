import dis

def f(x):
	return x * x

dis.dis(f)

# prints the following to console:

#   4           0 LOAD_FAST                0 (x)
#               2 LOAD_FAST                0 (x)
#               4 BINARY_MULTIPLY
#               6 RETURN_VALUE