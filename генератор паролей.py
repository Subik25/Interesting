user_name=''
while len(user_name.strip())<1:
 user_name=input('What is your name?\n')
print('It was nice to meet you,' + user_name + '!')
import random
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz1234567890+-/*!&$#?=@<>(),._'
number = input('Please enter the desired number of passwords:\n')
length = input('Please enter password length:\n')
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print("Your password:",'',password)