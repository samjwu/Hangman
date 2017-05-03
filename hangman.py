import getpass
import random

# answer = input("Enter a word to guess: ")

# answer = getpass.getpass()
# answer = answer.lower()


def getword():
    getdifficulty = True

    while getdifficulty:
        print("Select the difficulty:")
        print("1 - Easy")
        print("2 - Normal")
        print("3 - Hard")
        gamemode = input()

        try:
            if int(gamemode) == 1:
                lines = open("easy.txt").read()
            elif int(gamemode) == 2:
                lines = open("words.txt").read()
            elif int(gamemode) == 3:
                lines = open("hard.txt").read()
            else:
                print("Invalid input. Please enter a number from 1 to 3 inclusive.")
                continue
            getdifficulty = False

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    string = lines[0:]
    words = string.split()
    answer = random.choice(words)
    answer = answer.rstrip()
    return answer


def rungame():
    answer = getword()
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

                while True:
                    question = input("Play Again? (Y/N): ")
                    if question[0].lower() == 'n':
                        return False
                    elif question[0].lower() == 'y':
                        return True
                    else:
                        print("Invalid input. Enter either Y or N.")

        else:
            lives -= 1
            print("Guesses left: {}".format(lives))
            if lives == 0:
                print("\nYou Lose")
                print("\nThe word was: {}\n".format(answer))

                while True:
                    question = input("Play Again? (Y/N): ")
                    if question[0].lower() == 'n':
                        return False
                    elif question[0].lower() == 'y':
                        return True
                    else:
                        print("Invalid input. Enter either Y or N.")


playgame = True
while playgame:
    playgame = rungame()
