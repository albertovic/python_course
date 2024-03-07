#When outside mac uncomment
#from replit import clear
def add(n1,n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator(f_number, s_number, operator):
    function = operations[operator]
    return function(f_number, s_number)
    

new_calculation = True

while True:
    if new_calculation == True:
        f_number = float(input("\nWhat's the first number?: "))
    for symbol in operations:
        print(symbol)
    operator = input("Pick an operation: ")
    s_number = float(input("\nWhat's the second number?: "))
    calc_result = calculator(f_number, s_number, operator)

    print(f"\n{f_number} {operator} {s_number} = {calc_result}")

    if input(f"\nType 'y' to continue calculating with {calc_result}, or type 'n' to start a new calculation: ") == 'y':
        new_calculation = False
        f_number = calc_result
    else: 
        new_calculation = True
    
    #clear()