from generators import *

isActive = True
chances  = 4

##For the first time###########################################################
print("WELCOME!")

start_number = int(input("Enter your start number : "))
last_number  = int(input("Enter your last  number : "))

while last_number < start_number:
    print("WARNING:you can't make the last number smller then start number")
    last_number  = int(input("Enter your last  number : "))
##############################################################################


while isActive:
    user_guess   = int(input(f"Enter your guess number from {start_number} to {last_number}: "))
    result       = guess_generator(start_number , last_number , user_guess)
    
    print(result)

    minu = input("(q | quet) , (c | Change start/last number) press enter to countenu: ")

    if minu.lower() == "q":
        isActive = False
    elif minu.lower() == "c":
        start_number = int(input("Enter new start number : "))
        last_number  = int(input("Enter new last  number : "))

        while last_number < start_number:
            print("WARNING:you can't make the last number smller then start number")
            last_number  = int(input("Enter your last  number : "))