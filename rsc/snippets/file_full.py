with open('data.txt', 'r') as file:
	values = file.read().split(', ')

# if data.txt = "4, 10, 82, 15, 0"
# then will print ['4', '10', '82', '15', '0']
print(values)