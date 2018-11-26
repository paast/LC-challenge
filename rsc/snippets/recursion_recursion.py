def recursive_print(l):
	for item in l:
		if type(item) == type([]):
			recursive_print(item)
		else:
			print(item, end=' ')

my_list = [[1, 2], 3, [[4, 5], [6, 7]]]


# will print "1 2 3 4 5 6 7"
recursive_print(my_list)