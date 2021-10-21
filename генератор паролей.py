user_name=''
while len(user_name.strip())<1:
 user_name=input('What is your name?\n')
print('It was nice to meet you,' + user_name + '!')
import random
dictionary = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz1234567890+-/*!&$#?=@<>(),._'
number = int(input('Please enter the desired number of passwords:\n'))
length = int(input('Please enter password length:\n'))
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(dictionary)
    print("Your password:",'',password)