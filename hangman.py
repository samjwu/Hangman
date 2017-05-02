import getpass
import random

# answer = input("Enter a word to guess: ")

# print("Enter a word to guess")
# answer = getpass.getpass()
# answer = answer.lower()

print("Enter a number to select the difficulty:")
print("Easy - 1")
print("Normal - 2")
print("Hard - 3")
gamemode = input()

if int(gamemode) == 1:
    lines = open("easy.txt").read()
elif int(gamemode) == 2:
    lines = open("words.txt").read()
else:
    lines = open("hard.txt").read()

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
