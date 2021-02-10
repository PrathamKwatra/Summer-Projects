#Odd even game, Tells if the given number is even or odd and quits once a string is given

def odd_or_even(num):
	if num%2 == 0:
		return 1
	return 0

def game():
	try:
		num = int(input("Please input a number: "))
	except ValueError:
		return 1
	while num:
		oddEven = "even" if odd_or_even(num) == 1 else "odd"
		print(f"This {num} is an {oddEven} number!", end='')
		try:
			num = int(input("Give me another number: "))
		except ValueError:
			num = None
			print("String given. Exiting Game bye bye")
	return 0

if __name__ == "__main__":
	if game() == 1:
		print("Value Error. Bad input. Quiting Program")
	