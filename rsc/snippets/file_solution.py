# CSV
def primes(n):
	# left blank, returns primes list

primes = ','.join([str(n) for n in primes(1000)])

with open('primes.csv', 'w') as file:
	file.write(primes)


# JSON
import json

with open('challenge_3-2.json', 'r') as file:
	nums = json.loads(file.read())

print(sum(nums))