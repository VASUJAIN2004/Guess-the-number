# NUMBER GUESSING GAME 

# This program generates a random number between 1 and 100 and asks the user to guess it.
# The program will tell the user if the guess is too high or too low.
# The user is allowed to guess 10 times.
# If the user is unable to guess the number in 10 attempts, the program will display the number.
import random
print("Welcome to Number Guessing Game!")

# Generate a random number between 1 and 100.
num=random.randint(1,100)

# Initialize the number of attempts.

attempts=0

# Allow the user to guess 10 times.

while attempts<10:

    # Get the user's guess.

    guess=int(input("Guess a number between 1 and 100: "))
    attempts+=1
    # Check if the guess is too high or too low.
    if guess<num:
        print("Too low!")
    elif guess>num:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {num} correctly in {attempts} attempts.")
        break