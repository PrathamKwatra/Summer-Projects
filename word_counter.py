#word Count

def countWords(text):
	#Does not account for situations such as " lol ,  ;p , , , , , " this supposed to be 2 words. 
	text = text.split()
	return len(text)

def questionUser():
	print("Hey Buddy! Whats on your mind today?", end='\n')
	userInput = input("Answer: ")
	return userInput

def main():
	askUser = questionUser()
	print(f"You told me whats on your mind with {countWords(askUser)} word(s)")

if __name__ == "__main__":
	main()