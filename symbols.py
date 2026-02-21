import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
numbers = int(input("Choose the length of your password: "))
password = ""
for i in range(numbers):
    password += random.choice(symbols)
print("You are password is:",password)
