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
    
    operator_error = True

    while operator_error:
        operator = input("Pick an operation: ")
        if operator not in operations:
            print("\nChoose a valid operator.")
        else:
            s_number = float(input("\nWhat's the second number?: "))
            calc_result = calculator(f_number, s_number, operator)
            operator_error = False

    print(f"\n{f_number} {operator} {s_number} = {calc_result}")
    
    response_error = True

    while response_error == True:
        response = input(f"\nType 'y' to continue calculating with {calc_result}, 'n' to start a new calculation, or 'x' to exit: ")
        
        if response == 'y':
            new_calculation = False
            f_number = calc_result
            response_error = False
        elif response == 'n': 
            new_calculation = True
            response_error = False
        elif response == "x":
            print("\nExiting application...\n")
            exit()
        else: print("\nChoose a valid option.")
    
    #clear()