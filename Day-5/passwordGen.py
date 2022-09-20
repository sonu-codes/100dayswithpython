"""Day-5: Python password generator"""
import string
import random
#Crete a letters list
all_letters = string.ascii_letters
letters_list = []
for i in all_letters:
    letters_list.append(i)

# Create symbols list
symbols_list = ["!","@","#","$","%","^","&","*","(",")","_","+"]

#create Numbers list
number_list = list(range(10))

# take input from user
req_letters = int(input("How many letters:\n"))
req_symbols = int(input("How many symbols:\n"))
req_numbers = int(input("How many numbers:\n"))


password_list = []
for i in range(req_letters):
    password_list.append(random.choice(letters_list))

for j in range(req_symbols):
    password_list.append(str(random.choice(symbols_list)))

for k in range(req_numbers):
    password_list.append(str(random.choice(number_list)))

random.shuffle(password_list)

# convert list into string
password = ''
for i in password_list:
    password += i

print("Password:",password)