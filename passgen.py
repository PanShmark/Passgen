amount = 1
length = 16
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890#$%&*"
'''
Uppercase letters     ABCDEFGHIJKLMNOPQRSTUVWXYZ
Lowercase letters     abcdefghijklmnopqrstuvwxyz
Digits                1234567890
Special characters    #$%&*
'''

import random

while 1:
    for x in range(0,amount):
        password  = ""
        for x in range(0,length):
            password_chars = random.choice(chars)
            password = password + password_chars
        print(password)
    input()
