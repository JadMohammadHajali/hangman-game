""" Hangman Game Project

Is a guessing game, The program will choose a random animal name , and the play should guess
the animal name by calling letters.
"""
from wordslist import words
import random

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        print("-------------GUESS THE ANIMAL NAME-----------------")
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter A Letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input Please Enter A Character")
            continue

        if guess in guessed_letters:
            print(f"--{guess.upper()} Is Already Guessed--")
            continue

        guessed_letters.add(guess)

        if guess in answer:       # it will switch the underscore with the correct character
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:                       # with every mistake you make, it will build the body
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
