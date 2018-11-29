# number guessing program, where the computer guesses my number

def play_game(num):
    guess_ran = range(num)
    guess = (num/2)
    play = True
    while play:
        resp = input("Was {} your number? Higher (h), Lower (l), Correct (c)".format(guess))
        if resp == 'h':
            guess = guess_ran[round((len(guess_ran)/2))] + guess
            guess_ran = range[num/2, len(guess_ran)]
        elif resp == 'l':
            guess = guess - round((guess/2))
        elif resp == 'q':
            print("Fine, don't let me guess")
        elif resp == 'c':
            print('nailed it ')
            play = False


if __name__ == "__main__":
    r = input("would you like to play a game?: (y),(n),(q)")
    if r == 'y':
        num = int(input("guess numbers between 0 and what number?"))
        play_game(num)
    elif r == 'n':
        print("guess we're done then")
    elif r == 'q':
        print('still done')
    else:
        print("not an acceptable response")
