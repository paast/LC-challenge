from random import randrange

out = ""
t = 0
for n in spooky_mystery:
	x = str(randrange(-100, 100))
	y = str(randrange(-100, 100))
	z = str(randrange(-100, 100))
	t += randrange(1, 101)
	if n == '1':
		time = str(t)[::-1]
		x = x[::-1]
		y = y[::-1]
		z = z[::-1]
		out += "<{},{},{}>:[{}]".format(z,y,x,time)
	else:
		out += "[{}]:<{},{},{}>".format(t,x,y,z)

with open('bonnie.txt', 'w') as file:
	file.write(out)