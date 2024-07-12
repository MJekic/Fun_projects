#made to zero so user can change later for whatever they wish to do 
num1 = 0
num2 = 0

#ask the question of which operation to use 

operation = int(input("Which operation are you looking to do?\n 1. Addition +\n 2. Subtraction -\n 3. Multiplication *\n 4. Division /\n"))
while operation not in (1, 2, 3, 4):
    operation = int(input("Invalid operation selected\n   Enter valid response\n"))


num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))

if operation == 1:
    print("=",num1 + num2)
elif operation == 2:
    print("=",num1 - num2)
elif operation == 3:
    print("=",num1 * num2)
elif operation == 4:
    if num2 == 0:
        print("Cannot divide by zero ")
    else:
        print("=", num1 / num2)
   
