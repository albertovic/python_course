import random
from replit import clear
from stages import stages
from word_list import word_list

end_of_game = False
lives = 6
word = random.choice(word_list)

display = []

for char in word:
    display += '_'
    
print(display)

while not end_of_game:
    guess = input("\nGuess a letter: ")
    guess = guess.lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}...")
        lives -= 1
        print(stages[lives])
        if lives > 0:
            print(f"You have {lives} lives left.\n")
    else:
        for position in range(len(word)):
            if word[position] == guess:
                display[position] = guess

    if guess not in word:
        lives -= 1
        print(stages[lives])
        if lives > 0:
            print(f"You have {lives} lives left.\n")

    print(display)
    if lives == 0:
        print(f"\nYou loose! The word was {word}")
        exit()

    if '_' not in display:
        end_of_game = True
        print("\nYou win!")