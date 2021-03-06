import random


r = 20

graph = [['-' for _ in range(r)] for _ in range(r)]

heh = list(range(r))
random.shuffle(heh)
prev = None
for f in heh:
	if prev != None:
		graph[prev][f] = '0'
		graph[f][prev] = '0'
	prev = f

for f in range(r):
	n = random.randrange(3)
	for x in range(n):
		other = random.randrange(r)
		graph[f][other] = '0'
		graph[other][f] = '0'


output = ''
for line in graph:
	line = ' '.join([str(c) for c in line])
	print(line)
	output += line
	output += '\n'

with open('matrix.txt', 'w') as file:
	file.write(output)