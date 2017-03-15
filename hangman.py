import getpass

# answer = input("Enter a word to guess: ")
print("Enter a word to guess")
answer = getpass.getpass()

for n in range(100):
    print(" ")

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
    if guess in answer:
        guessedletters.append(guess)
        if len(guessedletters) == len(answer):
            print("\nYou Win!")
            print("\nThe word was: {}\n".format(answer))
            playgame = False
    else:
        lives -= 1
        print("Guesses left: {}".format(lives))
        if lives == 0:
            print("You Lose")
            playgame = False
