import random

num1 = random.randint(0,100)
num2 = random.randint(0,100)

operation = int(input("Which operation are you looking to do?\n 1. Addition +\n 2. Subtraction -\n 3. Multiplication *\n 4. Division /\n"))
while operation not in (1,2,3,4):
    operation = int(input("NOT A VALID RESPONSE\nType in new response here: "))

if operation == 1:
    answer = num1 + num2
    print(num1, "+", num2,"=")
    user_ans = float(input("What is the answer?\n "))
    if answer == user_ans:
        print("CORRECT!")
    while answer != user_ans:
            user_ans = float(input("INCORRECT TRY AGAIN\n   Type your answer here: "))
            if answer == user_ans:
                print("CORRECT!")
elif operation == 2:
    answer = num1 - num2
    print(num1, "-", num2,"=")
    user_ans = float(input("What is the answer?\n "))
    if answer == user_ans:
        print("CORRECT!")
    while answer != user_ans:
            user_ans = float(input("INCORRECT TRY AGAIN\n   Type your answer here: "))
            if answer == user_ans:
                print("CORRECT!")
elif operation == 3:
    answer = num1 * num2
    print(num1, "*", num2,"=")
    user_ans = float(input("What is the answer?\n "))
    if answer == user_ans:
        print("CORRECT!")
    while answer != user_ans:
            user_ans = float(input("INCORRECT TRY AGAIN\n   Type your answer here: "))
            if answer == user_ans:
                 print("CORRECT!")
else: 
    answer = num1 / num2
    print(num1,"/",num2,"=")
    user_ans = float(input("What is the answer?\n "))
    if answer == user_ans:
        print("CORRECT!")
    while answer != user_ans:
            user_ans = float(input("INCORRECT TRY AGAIN\n   Type your answer here: "))
            if answer == user_ans:
                 print("CORRECT!")

