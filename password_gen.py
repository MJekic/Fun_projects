import random

char = 'qwertyuiopasdfghjklzxcvbnm'
extra = "1234567890!@#$%^&*Z()"
password = "" #blank so we can create a new random one 
for i in range (10):
    x = random.randint(1,2)
    if x == 1:
        password += char[random.randint(0,25)] 
    else:
        password += extra[random.randint(0,20)]
print(password)