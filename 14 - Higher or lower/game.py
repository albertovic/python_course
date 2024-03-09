from random import randint
from os import system
import art
from game_data import data

DATA_LEN = len(data)

score = 0

#Function to print data
def print_comparison(n1, n2):
    print(f"Compare A: {data[n1]['name']}, a {data[n1]['description']}, from {data[n1]['country']}")
    print(art.vs)
    print(f"Against B: {data[n2]['name']}, a {data[n2]['description']}, from {data[n2]['country']}\n")

#Function to create two random numbers
def create_candidates():
    cand = []
    a_number = randint(0, DATA_LEN - 1)
    b_number = randint(0, DATA_LEN - 1)
    while(a_number == b_number):
        b_number = randint(0, DATA_LEN - 1)
    cand.append(a_number)
    cand.append(b_number)

    return cand

#Function? to compare the 2 values of followers
def compare_candidates(n1, n2, score):

    #User input
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == 'a':
        if data[n1]['follower_count'] > data[n2]['follower_count']:
            score += 1
            system('clear')
            print(art.logo)
            print(f"You're right! Current score: {score}")
        else:
            system('clear')
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()
            
    elif choice == 'b': 
        if data[n1]['follower_count'] < data[n2]['follower_count']:
            score += 1
            system('clear')
            print(art.logo)
            print(f"You're right! Current score: {score}")
        else:
            system('clear')
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()
    return score


#Game testing zone
print(art.logo)
while True:
    candidates = create_candidates()
    print_comparison(candidates[0], candidates[1])
    score = compare_candidates(candidates[0], candidates[1], score)