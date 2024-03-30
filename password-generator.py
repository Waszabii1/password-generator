import random
from colorama import Fore, init

init(autoreset=True)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!", "@", "£", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+", "-",
           "{", "}", "[", "]", ":", ";", "€", "|", "<", ">", "?", "/", "#", "."]

def main():
    print("Weak = Just letters \nMedium = Letters & Numbers \nStrong = Letters, Numbers & Special chars \nVery Strong = Letters, Numbers, Special chars & random capitalisation")
    while True:
        print("Type 'Weak', 'Medium', 'Strong' or 'VeryStrong' to get different strength passwords")
        pick = input().lower().replace(" ", "")
        length = int(input("How many characters do you want the password to be? "))
        if pick == "weak":
            weak(length)
            break
        elif pick == "medium":
            medium(length)
            break
        elif pick == "strong":
            strong(length)
            break
        elif pick == "verystrong":
            verystrong(length)
            break
        else:
            print("Invalid input, try again")
            continue

def weak(length):
    password = random.choices(letters, k=length)
    print("Your password is: " + Fore.RED + "".join(password))
    
def medium(length):
    choices = [letters, numbers]
    password = ""
    for i in range(length):
        password += str(random.choice(random.choices(choices, weights=map(len, choices))[0]))
    print("Your password is: " + Fore.RED + "".join(password))

def strong(length):
    choices = [letters, numbers, special]
    password = ""
    for i in range(length):
        password += str(random.choice(random.choices(choices, weights=map(len, choices))[0]))
    print("Your password is: " + Fore.RED + "".join(password))
    
def verystrong(length):
    choices = [letters, numbers, special]
    password = ""
    for i in range(length):
        password += str(random.choice(random.choices(choices, weights=map(len, choices))[0]))
    password = ''.join(random.choice((str.upper, str.lower))(i) for i in password)
    print("Your password is: " + Fore.RED + "".join(password))

if __name__ == "__main__":
    main()