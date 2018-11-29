import random

a = random.randint(0, 10)
play = True
num_turns = 0


while play:
    b = input("guess a number between 0 and 10 or 'q' to quit")
    if b == a:
        print ("you got it")
        play = False
    elif b == 'q':
        break
    else:
        print ("not quite, but try again!")
        num_turns += 1



print (num_turns)