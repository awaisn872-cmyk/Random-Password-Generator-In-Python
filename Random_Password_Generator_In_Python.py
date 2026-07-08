import string
import random

password_length=int(input("Enter the length of password: "))

charvalue=string.ascii_letters+string.digits

password=""
for i in range(password_length):
    password+=random.choice(charvalue)

print("\nYou random Password is: ",password)
