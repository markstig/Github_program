# This is a guess number game.

import random

print('Hello, what is your name?')
name = input('Please enter your name>>>> ')

print(f"Well, {name}, I am thinking a number between 1 to 100.")

secretNumber = random.randint(1, 100)


print('You have six times to guess the number.')

for i in range(1, 7):
    print('Take a guess')
    guess = int(input('Please enter your guess number: '))
    if guess < secretNumber:
        print('Your number is too low.')
    elif guess > secretNumber:
        print('Your number is too high.')
    else:
        break

if guess == secretNumber:
    print(f"Good job, {name}, you guessed my number!!!")
else:
    print('Nope, The number I was thinking of was ' + str(secretNumber))
