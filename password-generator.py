import random
from colorama import Fore

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
    pass

def medium():
    pass

def strong():
    pass

if __name__ == "__main__":
    print("Type 'weak', 'medium' or 'strong' to get different strength passwords")
    pick = input().lower()
    if pick == "weak":
        weak()
    if pick == "medium":
        medium()
    if pick == "strong":
        strong()
    else:
        print("Invalid input, try again")
        pick 
        
        

    