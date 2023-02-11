import sys
import random

def printStart():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    print()

if __name__ == '__main__':
    printStart()
    guess = 0
    i = 1
    secret = random.randint(1, 99)
    while guess != secret:
        guess = input("What's your guess between 1 and 99?\n>> ")
        if guess == "exit":
            print("Goodbye!")
            break
        try:
            guess = int(guess)
            if guess > secret:
                print("Too high!")
            elif guess < secret:
                print("Too low!")
            else:
                if i == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print("You won in " + str(i) + " attempts!")
                if secret == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
        except ValueError:
            print("That's not a number.")
        i += 1
