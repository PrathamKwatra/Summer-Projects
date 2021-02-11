import re

def askBio():
	print('Please input valid inforamtion. These characters are not allowed: #$%*!&@ and only 255 characters question.')
	userName = input("Hey, What is your name? ")
	userDob = input("Your Date of Birth: ")
	userAddress = input("Your Address Here: ")
	userBio = input("How would you describe yourself: ")
	allConditions = [ 
		(len(userName) <= 255) and (re_check(userName, 'name') == None), 
		(len(userDob) <= 255) and (re_check(userDob, 'date_of_birth') == None), 
		(len(userAddress) <= 255) and (re_check(userAddress, 'address') == None), 
		(len(userBio) <= 255) and (re_check(userBio, 'personal_bio') == None)
		]
	if all(allConditions):
		print('You Passed the first check! See you later!')
	else:
		print('You failed the check!')
		userChoice = input('Would you like to restart? Y/(any character)')
		if userChoice == 'Y':
			print('Restarting Program')
			main()
		print('Bye Bye')

def re_check(text, value):
	re_compile_dict = {
		'name':re.search(r'([!@#$%&*])', text), 
		'date_of_birth':re.search(r'([#$%*!&@])', text), 
		'address':re.search(r'([#$%*!@])', text), 
		'personal_bio':re.search(r'([#$%*!@])', text)
		}
	return re_compile_dict[value]

def main():
	askBio()

if __name__ == "__main__":
	main()