#!usr/bin/python3
"""
    They are imported to get a random word and to get an uppercase alphabet.
"""
import random
import string
import sys

def get_words(mstr):
    """
        This is created to get the words from the txt file.
    """
    try:
        with open(mstr, encoding="utf-8") as mfile:
            temp = mfile.readlines()
        return [element.strip() for element in temp]
    except FileNotFoundError:
        print(f'Your files does not exists: {mstr}. Please check')
        return False

def get_random_word(mlist):
    """
        This is created to randomly choose a word from the list.
    """
    try:
        word = random.choice(mlist).upper()
    except:
        print("Check the content in your file")
        sys.exit()
    return word
def display_hangman(tries):
    """
        This is created to display the stages.
    """
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def game(mstr):
    """
        This is the main code of the game.
    """
    curent = "_" * len(mstr)
    won = False
    letters = list(string.ascii_uppercase)
    chances = 6
    print("Let's play")
    print(display_hangman(chances))
    print(curent)
    print(*letters)
    while not won and chances > 0:
        try:
            turn = input("Enter a letter: ").upper()
            if len(turn) == 1 and turn.isalpha():
                if turn not in letters:
                    print("You already guessed it")
                elif turn not in mstr:
                    print("Unfortunate")
                    chances-=1
                    letters[letters.index(turn)] = "#"
                else:
                    print("Good,", turn, "is in the word!")
                    letters[letters.index(turn)] = "#"
                    temp = list(curent)
                    indices = [num for num, letter in enumerate(mstr) if letter == turn]
                    for index in indices:
                        temp[index] = turn
                    curent = "".join(temp)
                    if "_" not in curent:
                        won = True
            elif len(turn) == len(mstr) and turn.isalpha():
                if turn != mstr:
                    print(turn, "is not the word.")
                    chances -= 1
                else:
                    won = True
                    curent = mstr
            else:
                print("Not a valid guess.")
            print(display_hangman(chances))
            print(curent)
        except KeyboardInterrupt:
            print("\n")
            print("You interrupted the code!")
            sys.exit()
        if not won:
            print(*letters)
    if won:
        print("You guessed the word!")
    else:
        print("You ran out of tries. The word was", mstr)

def main():
    """
        This is the main
    """
    fname = "words.txt"
    words = get_words(fname)
    if words is False:
        sys.exit()
    word = get_random_word(words)
    print(word)
    game(word)
main()
