import random
import string

length = int(input("Enter the length of the password: "))
chars = string.ascii_letters + string.digits + string.punctuation

password = []  # empty list
for i in range(length):
    password.append(random.choice(chars))  # just append, do NOT assign

print(''.join(password))  # join list into string
