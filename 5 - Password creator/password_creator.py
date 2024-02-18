#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_characters = nr_letters + nr_symbols + nr_numbers

password = ''

lett_counter = 0
sym_counter = 0
num_counter = 0

for number in range(1, total_characters +1):
    flag = 0
    while flag == 0:
        rand_selector = random.randint(1, 3)
        if rand_selector == 1 and lett_counter < nr_letters:
            password = password + letters[random.randint(1, len(letters)-1)]
            lett_counter += 1
            flag = 1
        elif rand_selector == 2 and sym_counter < nr_symbols:
            password = password + symbols[random.randint(1, len(symbols)-1)]
            sym_counter += 1
            flag = 1
        elif rand_selector == 3 and num_counter < nr_numbers:
            password = password + numbers[random.randint(1, len(numbers)-1)]
            num_counter += 1
            flag = 1 

print(password)