import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#$%&*"
while 1:
    for x in range(0,1):
        password  = ""
        for x in range(0,16):
            password_chars = random.choice(chars)
            password      = password + password_chars
        print(password)
        input()
