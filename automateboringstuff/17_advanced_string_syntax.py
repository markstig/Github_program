# Escape Characters
print("That is Alice's cat.")
print('That is Alice\'s cat.')
print('Hello there! \nHow are you?\nI\'m fine.')

# raw string, we can use raw string to finish a sentence with many backslashes.
print(r'Hello')
print(r'Thant is Carole\'s cat.')

# Multipe strings with Triple Quotes

print('''
        Dear Alice, 
        Eve's cat has been arrested for catnapping, cat burglary,
        and extortion.
        Sincerely.
        ''')

# Similarities between strings and lists
spam = 'Hello World!'
print(spam[0])
print(spam[1:5])
print(spam[-1])
print('Hello' in spam)
print('x' in spam)
print('HELLO' in spam)
