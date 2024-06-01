import random

a=int(input("enter lower bound\n"))

b=int(input("enter upper bound\n"))

x=random.randint(a,b)

#it generates a random number in the range given as parameter

y=int(input("guess the number:\n"))

while(y!=x):
    if(y>x):
        print("your guess is high")
        y = int(input("guess the number:\n"))
    else:
        print("your guess is low")
        y = int(input("guess the number:\n"))

print("you won")