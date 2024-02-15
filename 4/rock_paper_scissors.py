import random

rps = ["Rock", "Paper", "Scissors"]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice < 0 or choice >= 3:
    print("Are you fucking around? SELECT A NUMBER FROM 0 TO 1 BITCH!")
    exit()
else:
    print(f"You choose {rps[choice]} \n")

computer = random.randint(0, 2)

print(f"Compute choose {rps[computer]}\n")

draw = "It's a draw!"

loose = "You lose"

win = "You win!"

win_conditions = [[draw, loose, win],[win, draw, loose],[loose, win, draw]]

print(win_conditions[choice][computer])