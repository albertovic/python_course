print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("Nice, you are tall enough!\n")
    age = int(input("How old are you?\n"))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Mid-life crisis tickets are free! Congratulations, you have a sad life.")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12
    

    wants_photo = input("\nDo you want a photo taken? Y or N\n")
    if wants_photo == "Y":
        bill += 3
    print(f"\nYour final bill is ${bill}. Try not to throw up...")
else:
    print("I'm sorry, come back when you grow up")