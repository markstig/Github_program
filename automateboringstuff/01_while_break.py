# Ask to enter a name, if enter the correct name, break the program.

while True:
    print('Who are you?')
    name = input()
    if name != 'Mark':
        continue
    print('Hello, Mark, What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.')
