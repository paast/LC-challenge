
try:
	file = open('filename', 'r')
	# do stuff with file
	file.close()

except IOError:
	print('file not found')