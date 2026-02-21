import random
number = int(input("Can you guess the number i think from 1 to 20,you have 5 chances!"))
comp = random.randint(1,20)
chances = 6
while chances>0:
  number = int(input("Enter your guess: "))
  if number>comp:
    print("Too high,try again!")
    chances -=1
  elif number<comp:
    print("That is too low,try again!")
    chances -=1
  elif number==comp:
    print("You get it! Congratulations!")
else:
  chances<=0
  print("You lose! The number was " + str(comp))
  
