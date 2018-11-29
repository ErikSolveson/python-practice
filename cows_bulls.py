#This program plays a game of cows and bulls with the user in which
# the user guesses a 4 digit number and the program gives feed back

import random


def generate_num ():
    return random.randrange(1000,9999)

def play_game():
    num = generate_num()
    num = str(num)
    print(num)
    play = True
    while play:
        guess = input("enter your 4 digit guess: ")
        bulls = 0
        cows = 0
        for i in range(4):
            if guess[i] in num:
                if guess[i] == num[i]:
                    cows += 1
                else:
                    bulls += 1
            else:
                i += 1
        if cows == 4:
            print("you got it!")
            break
        else:
            print("Cows: {}, Bulls: {}".format(cows,bulls))


if __name__=="__main__":
    play = input("Would you like to play a game?: (y),(n)")
    if play == "y":
        play_game()
    else:
        print("see you later!")