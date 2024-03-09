import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def compare(number, guess):
    """
    Compares the guess with the random number. Returns 1 if its not equal and 0 if its equal.
    """
    if guess > number:
        print("Too high.")
        print("Guess again.")
        return 1
    elif guess < number:
        print("Too low.")
        print("Guess again.")
        return 1
    elif guess == number:
        return 0

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS

def game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)

    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if compare(number, guess) == 1:
            attempts -= 1
        else:
            print(f"You got it! The answer was {number}.")
            exit()

    print("You've run out of guesses, you lose.")

game()