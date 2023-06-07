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
    while points > 0:#we open our first cycle, start comparing if points is greater than 0 you can continue.
    #we ask the user to enter their first try
        attempt = int(input("Try to guess the number, enter the number you think it is: "))
        #If the first cycle is fulfilled, 
        #it compares if the number entered by the user is correct, if it is correct, it continues.
        if attempt == numer:
            points += 10
            #shows that it is correct and ends.
            print("Congratulations you have discovered the number : ")
            print("Game over")
            break
        else:#If the if cycle is not fulfilled, they continue 
        #with the else and this is repeated until if is fulfilled, 
        #all this taking into account that we still have points.
            points -= 10
            print("Sorry, your answer is incorrect, please try again.  ")
            print("Your performance points are: ",points)
          #if it runs out of points, it shows you a message and the correct answer.
        if points == 0:
         print("Your opportunities have been exhausted. We are sorry.  The number to guess is wrong:", numer)
         print("Game over ")

random_number()