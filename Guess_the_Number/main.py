import art
import random
print(art.logo)
print("Welcome to Guessing Game!\n")
print("You can choose a number between 1 and 100.\n")
choice = input("Choose a difficulty level:'easy' or 'hard':").lower()
chosen_number = random.randint(1, 100)
if choice == "easy":
    number_of_attempts = 10
elif choice == "hard":
    number_of_attempts = 5
else:
    print("Enter valid input")
    exit()

while number_of_attempts > 0:
        print(f"You have {number_of_attempts}  attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if  guess > chosen_number:
            print("Too high!")
            print("Guess again.")
            number_of_attempts = number_of_attempts - 1
        elif guess < chosen_number:
            print("Too low!")
            print("Guess again.")
            number_of_attempts = number_of_attempts - 1
        else:
            print(f"You got it! The answer was {chosen_number}.")
            break
print(f"The Number is {chosen_number}.")
