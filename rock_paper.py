import random

replay = 1
while replay == 1:
# Printing starting screen that asks the question to the user 
    print("---------------")
    print(" 1. Rock✊\n 2. Paper🖐\n 3. Scissors✌")
    print("---------------")

# Input to ask them to pick which sign they wanna use and while loop to make them from picking a wrong input 
    rps = int(input("Pick a number: "))
    while rps not in (1,2,3):
        rps = int(input("Invalid Input Type In Correct Input\n"))

# To pick computers sign that they throw out
    cpu = random.randint(1,3)

    signs = {1:"Rock✊",2:"Paper🖐",3:"Scissors✌"}
    print(f"CPU picks {signs[cpu]}\n" + f"Player picks {signs[rps]}")

# All posibble outcomes for the game and the messages 
    if rps == 1 and cpu == 3:
        print("Player Wins!")
    elif rps == 2 and cpu == 1:
        print("Player Wins!")
    elif rps == 3 and cpu == 2:
        print("Player Wins!")
    elif rps == cpu:
        print("It's a Tie")
    else:
        print("CPU Wins")
    replay = int(input("Do you wish to replay\n 1.Yes\n 2.No\n"))
    while replay not in (1,2):
        replay = int(input("Invalid input type in valid one\n"))