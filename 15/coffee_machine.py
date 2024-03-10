#Imports
import menu

#Initial ammounts
INITIAL_WATER = menu.resources["water"]
INITIAL_MILK = menu.resources["milk"]
INITIAL_COFFEE = menu.resources["coffee"]
INITIAL_MONEY = 0

#Initial assignments
water = INITIAL_WATER
milk = INITIAL_MILK
coffee = INITIAL_COFFEE
money_ammount = INITIAL_MONEY

def print_report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: ${money_ammount}")

def check_resources(type):
    """
    Returns -1 if there is something missing and prints the missing ingredients. Returns 0 if everything is OK.
    """
    sorry_string = "\nSorry, there is not enough "

    lack_flag = 0

    if water < menu.MENU[type]["ingredients"]["water"]:
        sorry_string += "water "
        lack_flag = 1
    if coffee < menu.MENU[type]["ingredients"]["coffee"]:
        sorry_string += "coffee "
        lack_flag = 1
    if type != "espresso":
        if milk < menu.MENU[type]["ingredients"]["milk"]:
            sorry_string += "milk "
            lack_flag = 1

    if lack_flag == 1:
        print(sorry_string)
        return -1
    else:
        return 0

def process_coins():
    """
    Asks for the coins, adds them and returns the total value in dollars.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("Hoy many nickles?: "))
    pennies = int(input("How many pennies?: "))

    return (quarters*0.5 + dimes*0.1 + nickles*0.05 + pennies*0.01)

def check_transaction(type, money):
    """
    Returns the amount of money that should get storaged. If not succesful, returns -1
    """
    if money < menu.MENU[type]["cost"]:
        print("\nSorry that's not enough money. Money refunded.")
        return -1
    elif money == menu.MENU[type]["cost"]:
        return money
    elif money > menu.MENU[type]["cost"]:
        change = round(money - menu.MENU[type]["cost"],2)
        print(f"\nHere is ${change} in change.")
        return menu.MENU[type]["cost"]



#Main
keep_refilling = "y"
print_report()
while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print_report()
    elif choice == "refill":
        while keep_refilling == "y":
            refill_choice = input("\nWhat would you like to refill? (water/milk/coffee): ").lower()
            refill_amount = int(input("What amount would you like to insert? (g or ml): "))

            if refill_choice == "water":
                water += refill_amount
            elif refill_choice == "coffee":
                coffee += refill_amount
            elif refill_choice == "milk":
                milk += refill_amount
            
            keep_refilling = input("Would you like to refill another ingredient? Type 'y' or 'n': ").lower()
    elif check_resources(choice) == 0:
        coin_input = process_coins()
        if check_transaction(type=choice, money=coin_input) > 0:
            money_ammount += menu.MENU[choice]["cost"]
            print(f"\nHere is your {choice}. Enjoy!")
            water -= menu.MENU[choice]["ingredients"]["water"]
            coffee -= menu.MENU[choice]["ingredients"]["coffee"]
            if choice != "espresso":
                milk -= menu.MENU[choice]["ingredients"]["milk"]

