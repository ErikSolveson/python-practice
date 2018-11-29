import random


def open_file(file):
    words = []
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            line.strip()
            words.append(line)
            line = f.readline()
    return words  # returns a list of all the words in the file


def pick_random(words):
    rand_index = random.randint(0, len(words))
    return words[rand_index] # picks a random index from the entire length of the list


def player_guess():  # returns just one letter that is an input from a user
    valid_guess = True
    while valid_guess:
        guess = input("what letter would you like to guess: ")
        if len(guess) > 1:
            print("please only input one character")
        elif guess.isnumeric():
            print("please enter only one letter")
        else:
            return guess


def calculate_guess(word, guess):
    display = "_" * len(word)
    for i in range(len(word)):
        for j in range(len(guess)):
            if word[i] == guess[j]:
                print("word = guess")
                print(word[i])
                print(i)
                display = display[i].replace(display[i], word[i])
                print(display)

            elif word[i] != guess[j]:
                continue
    return display


if __name__ == "__main__":
    play_game = True
    guess = ""

    word = pick_random(open_file("/Users/erik.solveson/PycharmProjects/untitled/sowpods.txt"))
    print(word)
    guess = guess + player_guess()
    display = calculate_guess(word, guess)
    print(display)



