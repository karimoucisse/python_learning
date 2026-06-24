import random

def main() :
	print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")
	min = int(input("select min number range: "))
	max = int(input("select max number range: "))
	while(min >= max):
		max = int(input("Min can't be >= max, Select a new max number: "))
	print(f"\nYou have 7 chances to guess the number between {min} and {max}. Let's start!")
	val = random.randrange(min, max, 3)
	life = 7
	while(1) :
		if(not life):
			print("Game Over!")
			return
		guess_val = int(input("select a number: "))
		if(guess_val == val):
			print("Correct!")
			return
		elif(guess_val > val):
			print("Too high")
		else:
			print("Too low")
		life -= 1
	print("Game Over!")


if __name__ == "__main__":
	main()

