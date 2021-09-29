# Number guessing game
# imported random function for
# generate random numbers
import random
import math

# guess the lower number
lower = int(input("Enter lower number : "))
# guess the higher number
upper = int(input("Enter upper number : "))

# guess count is zero while beggining
count = 0

# total guess number
numberOfGuess = 5
print(f"You have {numberOfGuess} chance to guess currect number\n")

# genereting the random number
randomNumber = random.randint(lower, upper)

# guess the number and if it's currect
# make the congratulation messages
while count < math.log(upper - lower + 1, 2):
	# take the guess number
	guessNumber = int(input("Guess the number : "))
	count = count + 1

	# condition if value is high
	if guessNumber > randomNumber:
		print("This is too high!")

	# condition if value is low
	elif guessNumber < randomNumber:
		print("This is too low!")

	# guess is currect
	elif guessNumber == randomNumber:
		print("Congratulations, You guess the currect number!")
		break

# say good buy
print("This the the END of the game!")

