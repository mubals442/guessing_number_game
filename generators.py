import random

def guess_generator(start_number , last_number , guess):
    random_number = random.randint(start_number , last_number)

    if guess == random_number:
        return(f"WIN! \nANSWER:{random_number}")
    elif  guess < start_number or guess > last_number:
        return("NOT FOUND")
    else:
        return(f"LOSE! \nANSWER:{random_number}")