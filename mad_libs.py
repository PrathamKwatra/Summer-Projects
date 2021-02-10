#3 sentence Poem Mad libs

from random import randint as rint

def mad_libs(word_1, word_2, word_3):
	mad_libs = {
		1: f"Roses are {word_1},\n\tViolets are {word_2},\nI love {word_3}", 
		2: f"{word_1} are crazy,\n\tmy life is {word_2},\nHope you have a {word_3} day", 
		3: f"These {word_1} are nice,\n\t These are supposed to be {word_2},\nSadly they are {word_3}", 
		4: f"I do not know {word_1} things\n\t But I do know {word_2} and,\nWould like to learn {word_3} things", 
		5: f"These are {word_1} libs,\n\t I prefer Atlas and {word_2} stuff,\nI hate {word_3} related things"}
	print(mad_libs[rint(1,5)])
	print("Thanks for playing !")

def user_inputs():
	word_1 = input("Enter the first word: ")
	word_2 = input("Enter the second word: ")
	word_3 = input("Enter the third word: ")w
	mad_libs(word_1, word_2,  word_3)

def game_start():
	print("Hey! This is a Mad Libs game. Please Enter Three words to start! ")
	user_inputs()

if __name__ == "__main__":
	game_start()