print("Welcome to The Treasure Island!\n")
print("You are trying to get the treasure from the island you just arrived to.")
print("In front of you there is a fork.")
print("The left path leads to a sunny and apparently safe area. However, there is a sign that reads 'DO NOT GO THIS WAY'")
print("The right pach leads to a more obscure and neglected area. There is no sign\n")
first_decission = input("Where do you want to go? Type 'left' or 'right': \n")

if first_decission == "right":
    print("\nYou encounter a puppy and bend over to pet it. As you reach its head with your hand it bites you and tears your arm. You are DEAD!\n")
elif first_decission == "left":
    print("\nYou get to a calm lake. At the opposite shore you can glimpse something shiny. There is a small boat next to you.\n")
    second_decission = input("Will you cross the lake swimming or with the boat? Type 'swimming' or 'boat':\n")
    if second_decission == "swimming":
        print("\nWhat is wrong with you? As soon as you entered the water a bank of piranhas ate you entirely. You are DEAD!\n")
    elif second_decission == "boat":
        print("\nYou take the boat and sail to the other shore. The shiny object laying on the ground seems to have a dark aura...\n")
        third_decission = input("Will you pick it or will you go away? Type 'pick it' or 'leave it':\n")
        if third_decission == "pick it":
            print("\nYou greedy bastard... The shiny object appears to be a necklace. You put it on. Immediately, you get possesed by a deadly force, consuming your soul. You are DEAD!\n")
        elif third_decission == "leave it":
            print("\nYou go away, leaving the mysterious treasure untouched. You come back to the entrance of the island and find an old lady.")
            print("\nShe approaches you without saying a word and hands you a key... maybe for another adventure?")