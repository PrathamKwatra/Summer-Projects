#Acronym Creator
import re

#def checkInput(text):
#	return re.search(r'([!@#$%&*0-9])', text)

def createAcronym(text):
	print('Creating Acronyms of the capital letters')
	listText = text.split()
#	print(listText)
	acroymToPrint = ''
	for i in listText:
		reg_result = re.search(r'([A-Z])', i)
		if reg_result != None:
			acroymToPrint += str(reg_result.group())
	print(acroymToPrint)


def main():
	print('Hey there! I can help create acronyms of any input you give!\nIt just needs to any A-Z in the beginning')
	userInput = input('Input Text here: ')
	createAcronym(userInput)

if __name__ == '__main__':
	createAcronym('Nicely Done but NO. THIS IS IN O(N)')