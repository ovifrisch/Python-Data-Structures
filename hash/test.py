import math

def is_prime(num):
	for i in range(2, math.floor(pow(num, 0.5))):
		if (num % i == 0):
			print(i)
			return False
	return True

"""
find the first prime greater than N
"""
def next_prime(N):
	curr = N + 1
	next_prime = None
	while (not next_prime):
		prime = True
		for i in range(2, math.floor(pow(curr, 0.5)) + 1):
			if (curr % i == 0):
				prime = False
				break
		if (prime):
			next_prime = curr
		curr += 1
	return next_prime

def firstNPrimes(offset, N):
	res = []
	curr_num = max(3, offset + 1)
	while (len(res) < N):
		prime = True
		for i in range(2, math.floor(pow(curr_num, 0.5)) + 1):
			if (curr_num % i == 0):
				prime = False
				break
		if (prime):
			res.append(curr_num)
		curr_num += 1
	return res


print(firstNPrimes(100, 1))
print(next_prime(101))
print(is_prime(103))


