import random
import time
import string

startTime = time.time()

password = input ("Enter the password: ")

char = list(string.printable)


def crack(password):
    attemps = 0
    while True: 
        var = random.choices(char, k=len(password))
        print(">>>>", var, "<<<<")
        ps = "".join(var)
        attemps += 1
        if password == ps:
            print("Your password is:", ps)
            return attemps
            break;


endTime = time.time()
elapsedTime = endTime - startTime
attempts = crack(password)
print(f"This took {elapsedTime} seconds to crack")
print(f"and took {attempts} attempts!")