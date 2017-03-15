import getpass
import random

# answer = input("Enter a word to guess: ")

# print("Enter a word to guess")
# answer = getpass.getpass()
# answer = answer.lower()

lines = open("words.txt").read()
string = lines[0:]
words = string.split()
answer = random.choice(words)
answer = answer.rstrip()

playgame = True
guessedletters = set()
lives = 10

while playgame:
    for letter in answer:
        if letter in guessedletters:
            print(letter, end = " ")
        else:
            print("_", end = " ")

    guess = input("Guess a letter: ")
    guess = guess.lower()
    guess = guess.rstrip()

    if guess in answer:
        guessedletters.add(guess)
        if len(guessedletters) == len(answer):
            print("\nYou Win!")
            print("\nThe word was: {}\n".format(answer))
            playgame = False
    else:
        lives -= 1
        print("Guesses left: {}".format(lives))
        if lives == 0:
            print("\nYou Lose")
            print("\nThe word was: {}\n".format(answer))
            playgame = False
