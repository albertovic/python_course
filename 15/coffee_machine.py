#Initial ammounts
INITIAL_WATER = 300
INITIAL_MILK = 200
INITIAL_COFFEE = 100
INITIAL_MONEY = 0

#TODO 1: Print report
def print_report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


#TODO 2: Check if resources are sufficient
"""
Espresso $1,50:
    - Water: 50ml
    - Coffee: 18g

Latte $2,50:
    - Water: 200ml
    - Coffee: 24g
    - Milk: 150ml

Capuccino $3,00:
    - Water: 250ml
    - Coffee: 24g
    - Milk: 100ml
"""


def check_resources(type):
    sorry_string = "Sorry, there is not enough "
    if type == "espresso":
        if water < 



#TODO 3: Process coins

#TODO 4: Check if the transaction is successful

#TODO 5: Make the coffee

#TODO 6: Substract the ingredients used and add the money to the machine


