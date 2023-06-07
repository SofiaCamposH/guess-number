import random #we import the function random

def random_number():
    print("To start you must enter the range which you want to guess.")
    #It asks the user to enter a high and a low at which the range will start and end.
    ran_one = int(input("Enters the first minimum range: "))
    ran_two = int(input("Enter the second maximum range: "))
    #We use the function already mentioned, to this we give the initial number and the final number.
    # Calculates a random number among the entered numbers.
    numer = random.randint(ran_one, ran_two) 
    points = 100#We start points at 100, because it is what it starts with and so that the cycle can start.
    