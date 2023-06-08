from getpass import getpass
player1points=100
player2= getpass("write random number: ") #getpass to keep the number hidden in the console
#cycle for the player to guess the number
while True:
   player1= input("Try to guess the number: ")
   if player1 == player2:
    print("Congratulations,did you guess the number, you have: ",(player1points))
    break