# Password Generator for characters and symbols

import random
import time


def get_ran_char ():
    return chr(random.randint(65,122))


def make_password(length):
    password = []
    for i in range(length):
        password.append(get_ran_char())
    password = ''.join(password)
    return password


length = int(input("How long would you like your password? "))
start_time = time.time()
print ("starting time {}".format(start_time))
password = make_password(length)
print (password)
print ("Elapsed time: {}seconds".format(round(time.time() - start_time)))


