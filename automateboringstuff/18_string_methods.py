# upper and lower string method
spam = 'Hello World!'
print(spam.upper())
print(spam.lower())

print(spam)

spam = spam.lower()  # this changes the spam
print(spam)

# answer = input('Please enter yes: ')
# if answer.lower() == 'yes':
# print('Correct!')

# isupper and islower
spam = 'Hellow wrold!'
print(spam.islower())
spam = 'HELLOW WORLD!'
print(spam.isupper())
print('Hello'.upper().isupper())

print('----------------')

print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print('hello world'[5].isspace())

print('This Is Title Case.'.istitle())
print('hello world!'.title())

print('----------------')
# startwith() endwith()
print('Hellow world!'.startswith('Hello'))
print('Hellow world!'.endswith('world!'))

# join()
print(', '.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print('\n\n'.join(['cats', 'rats', 'bats']))

# split()
print('My name is Simon'.split())
print('My name is Simon'.split('m'))

# ljust(), rjust()
print('Hello'.rjust(10))
print('Hello'.rjust(20, '*'))
print('hello'.ljust(25, '-'))

# center()
print('Hello'.center(20))
print('Hello'.center(20, '='))

# stip() rstrip() lstrip()
print('     x     '.strip())
print('     x     '.lstrip())
print('     x     '.rstrip())
print('SpamSpamBasonSpamEggsSpamSpam'.strip('am'))

# replace()
spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))
