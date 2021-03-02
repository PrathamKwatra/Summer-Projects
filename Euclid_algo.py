#Euclid's Algorithm

import math

def gcd(a, b):
	if b == 0:
		return a
	if a > b:
		a, b = b, a
	print(a, b)
	b = b % a
	return gcd(a, b) 

if __name__ == '__main__':
	print(gcd(28,300))