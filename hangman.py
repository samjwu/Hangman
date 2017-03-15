import getpass
import random
# import sys
# import termios
# import fcntl
# import os

# def Getch():
#     fd = sys.stdin.fileno()
#
#     oldterm = termios.tcgetattr(fd)
#     newattr = termios.tcgetattr(fd)
#     newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
#     termios.tcsetattr(fd, termios.TCSANOW, newattr)
#
#     oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
#     fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
#
#     try:
#         while 1:
#             try:
#                 c = sys.stdin.read(1)
#                 break
#             except IOError: pass
#     finally:
#         termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
#         fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
#     return c


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
guessedletters = []
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
    # print("Guess a letter: ")
    # guess = Getch()
    if guess in answer:
        guessedletters.append(guess)
        if len(guessedletters) == len(answer)-1:
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
