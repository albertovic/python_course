from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(plain_text, shift):
    output = ''
    for letter in plain_text:
        if letter not in alphabet:
            output += letter
        else:
            index = alphabet.index(letter)
            index += shift
            while index < 0 or index >= (len(alphabet)-1):
                if (index > 0) and (index > (len(alphabet)-1)):
                    index = index - len(alphabet)
                    print(index)
                elif (index < 0) and index < (len(alphabet)):
                    index = len(alphabet)+index
                
            output += alphabet[index]
    
    return output

flag = 'y'

while flag == 'y':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    if direction == 'decode':
        shift = -shift
        print("The decoded text is", caesar_cipher(plain_text=text, shift=shift))
    else:
        print("The encoded text is", caesar_cipher(text, shift))

    flag = input("\nIf you want to keep using the Caesar Cipher write Y. If not, write N.\n").lower()

    clear()
    


