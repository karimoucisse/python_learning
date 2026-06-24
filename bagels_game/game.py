import random

def main():
	max = 999
	min = 100
	max_guess = 10
	val = str(random.randrange(min, max, 3))
	print("I am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\n")
	print("Pico : One digit is correct but in the wrong position.\n")
	print("Fermi : One digit is correct and in the right position.\n")
	print("Bagels : No digit is correct.\n")
	while(1):
		if(max_guess == 0):
			return print("GAME OVER!")
		guess_val = input("guess value: ")
		if guess_val == val :
			return print("You got it!")
		i = 0
		res = 0
		while i < len(guess_val):
			if guess_val[i] == val[i] :
				res += 1
				print("Fermi")
			elif val.find(guess_val[i]) != -1:
				res += 1
				print("Pico")
			i += 1
		if(res == 0):
			print("Bagels")
		max_guess -=1

if __name__ == "__main__":
	main()
