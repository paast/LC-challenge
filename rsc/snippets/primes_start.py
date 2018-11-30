# prime time starter code

def is_prime(n):
	for num in range(2, n):
		if n % num == 0:
			return False
	return True

def primes(n):
	prime_list = []
	for num in range(2, n + 1):
		if is_prime(num):
			prime_list.append(num)
	return prime_list