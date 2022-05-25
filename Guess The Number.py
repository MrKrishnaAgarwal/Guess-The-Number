from random import randint

print("Hello! What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 10.")
secretNumber = randint(1, 10)

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        print ("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses!")
        break