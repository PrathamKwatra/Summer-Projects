#Euclid's Algorithm

import math

#iterative Solution
def e_gcd(a, b):
	# if a > b:
	# 	a, b = b, a
	x,y , w, z = 0,1 , 1,0
	while a != 0:
		print(f"a:{a}, b:{b}, x:{x}, y:{y}, w:{w}, z:{z}")
		q,r = b//a, b%a
		m, n = x-w*q, y-z*q
		b,a, x,y, w,z = a,r, w,z, m,n
		
	gcd = b
	return gcd, a, b

def gcd(a, b):
	if b == 0:
		return a
	if a > b:
		a, b = b, a
	print(a, b, b%a)
	b = b % a
	return gcd(a, b) 

if __name__ == '__main__':
	print(gcd(26,15))