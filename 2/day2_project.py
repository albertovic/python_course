print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

tota_in_float = float(total)
percentage_in_float = float(percentage)
num_people_in_float = float(num_people)

percentage_multiplier = 1 + (percentage_in_float/100)
bill_with_tip = tota_in_float * percentage_multiplier
price_per_person = round(bill_with_tip/num_people_in_float, 2)

print(f"Each person should pay: ${price_per_person}")