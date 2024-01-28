import random
from colorama import Fore, init

init(autoreset=True)

letters = ["a", "b", "c", "d", "e", "f", "g",
           "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u"
           "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4",
           "5", "6", "7", "8", "9"]
special = ["!", "@", "£", "$", "%", "^", "&",
           "*", "(", ")", "-", "=", "+", "-",
           "{", "}", "[", "]", ":", ";", "€",
           "|", "<", ">", "?", "/", "#", "."]

def weak():
    print("How long do you want your password to be? ")
    length = int(input())
    password = random.choices(letters, k=length)
    print("Your password is: " + Fore.RED + "".join(password))
    
def medium():
    choices = [letters, numbers]
    print("How long do you want your password to be?")
    length = int(input())
    password = ""
    for i in range(length):
        password += str(random.choice(random.choices(choices, weights=map(len, choices))[0]))
    print("Your password is: " + Fore.RED + "".join(password))

def strong():
    choices = [letters, numbers, special]
    print("How long do you want your password to be?")
    length = int(input())
    password = ""
    for i in range(length):
        password += str(random.choice(random.choices(choices, weights=map(len, choices))[0]))
    print("Your password is: " + Fore.RED + "".join(password))
    
def verystrong():
    choices = [letters, numbers, special]
    print("How long do you want your password to be?")
    length = int(input())
    password = ""
    for i in range(length):
        password += str(random.choice(random.choices(choices, weights=map(len, choices))[0]))
    password = ''.join(random.choice((str.upper, str.lower))(i) for i in password)
    print("Your password is: " + Fore.RED + "".join(password))

if __name__ == "__main__":
    print("Weak = Just letters \nMedium = Letters & Numbers \nStrong = Letters, Numbers & Special chars \nVery Strong = Letters, Numbers, Special chars & random capitalisation")
    while True:
        print("Type 'weak', 'medium', 'strong' or 'verystrong' to get different strength passwords")
        pick = input().lower()
        if pick == "weak":
            weak()
            break
        elif pick == "medium":
            medium()
            break
        elif pick == "strong":
            strong()
            break
        elif pick == "verystrong":
            verystrong()
            break
        elif pick != "weak" or "medium" or "strong":
            print("Invalid input, try again")
            continue
 
        
        

    