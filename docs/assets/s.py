
with open('matrix.txt') as file:
	lines = [line.strip().split(' ') for line in file.readlines()]

chars = [[] for _ in range(20)]
for i, line in enumerate(lines):
	for j, char in enumerate(line):
		if char == '0':
			chars[i].append(chr(j + 65))

for i, char in enumerate(chars):
	print(f"{chr(i + 65)}: {char}")