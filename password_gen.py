import random

abc = 'abcdefghijklmnopqrstuvwxyz'
extras = '0123456789_!*&$%?><.'
new_password = ''#empty string
for i in range(16): #password length
    x = random.randint(1,2)
    if x == 1:
        new_password += abc[random.randint(0,16)]
    else:
        new_password += extras[random.randint(0,16)]
print(new_password)