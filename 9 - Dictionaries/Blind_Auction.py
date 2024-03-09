from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program!")

bidders = {}
flag = 1

name = ""
bid = 0

def find_max_value(dict):
    old_val = 0
    winner_name = ''
    
    for key in dict:
        # print(type(int(dict[key])))
        val = int(dict[key])
        if val > old_val:
            winner_name = key
            old_val = val
    
    print(f"The winner is {winner_name} with a bid of ${val}.")


while (flag == 1):
    name = input("\nWhat is your name?: ")
    bid = input("\nWhat's your bid?: $")

    bidders[name] = bid

    if input("\nAre there any other bidders? Type 'yes' or 'no'.\n").lower() == "no":
        flag = 0
    
    clear()

find_max_value(bidders)

# print(bidders)