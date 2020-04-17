# Random a number, copy it to system clipboard, then exit the program

import random, sys, pyperclip

num = random.randint(0, 10)

pyperclip.copy('This is a random number: ' + str(num))

number = pyperclip.paste()

print(number)

print('Now we use sys.exit() to exit the program')
sys.exit()

print('This line will not be shown becaue we have exited the program')



