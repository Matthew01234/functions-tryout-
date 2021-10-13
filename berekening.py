import random


optel1 = random.randint(0,1000)
optel2 = random.randint(0,1000)
def addition (number1,number2):
    return number1 + number2
for i in range (3):
    print (str(optel1) + ' + '  + str(optel2)+' = ' + str(addition(optel1,optel2)))
    optel1 = random.randint(0,1000)
    optel2 = random.randint(0,1000)

print ()

min1 = random.randint(0,1000)
min2 = random.randint(0,1000)
def subtraction (number1b,number2b):
    return number1b - number2b
for i in range (3):
    print (str(min1) + ' - '  + str(min2)+' = ' + str(subtraction(min1,min2)))
    min1 = random.randint(0,1000)
    min2 = random.randint(0,1000)

print ()
keer1 = random.randint(0,1000)
keer2 = random.randint(0,1000)
def multiplication (number1c,number2c):
    return number1c * number2c
for i in range (3):
    print (str(keer1) + ' x '  + str(keer2)+' = ' + str(multiplication(keer1,keer2)))
    keer1 = random.randint(0,1000)
    keer2 = random.randint(0,1000)



print ()
increment1 = random.randint(0,1000)

def increment (number1e,number2e):
    return number1e + number2e
for i in range (3):
    print (str(increment1) + ' + 1 = '  + str(int(increment(increment1, 1))))
    increment1 = random.randint(0,1000)
   

print ()
decrement1 = random.randint(0,1000)

def decrement (number1f,number2f):
    return number1f - number2f
for i in range (3):
    print (str(decrement1) + ' - 1 = '  + str(int(decrement(decrement1, 1))))
    decrement1 = random.randint(0,1000)