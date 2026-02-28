import random 
symbols = "!@#$%^&*()_+{:><~"
user = int(input("Enter the length of the password:"))
password=""
for i in range(user):
    password = password+random.choice(symbols)
print("Your new password is:",password)

for i in range(1,6):
   print(i*"$")

name = input("Enter your name:")
print("Your name is:",name)
print("*********")
print("*",name,"*")
print("*********")

n = int(input("Enter the number:"))
print(sum(range(1,1+n)))


import random
chances = 5
game = input("HI! Welcome to our game,Guess The Number Are you ready? Yes or No?")
if game == "No":
    print("Fine! That is your decision")
elif game == "Yes":
   print("Let's get started")
    
   comp = random.randint(1,20)
   while chances>0:
    number = int(input("Enter the number between 1 to 20"))   
    if number>comp:
        print("Oh bro that is too much")
        chances -=1
    elif number<comp:
        print("It is too few,try again")
        chances -=1
    elif number==comp:
        print("Congratulations! You got it")
        break

    if chances == 0:
        print("You lose your chances, the nmuber was",comp)