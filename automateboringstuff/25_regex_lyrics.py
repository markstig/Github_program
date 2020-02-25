import re

lyrics = ''' 12 drummers drumming, 11 pipers piping, 10 lords a leaping, 
9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying,
5 golden rings, 4 calling birds, 3 french hens, 2 turtles doves, 
and 1 partridge in a pear tree.
'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(
    r'[aeiou]')  # this is the same with re.compile(r'a|e|i|o|u')
# vowelRegex = re.compile(r'[a-zA-F]') # here means all characters, from a to z and A to F
print(vowelRegex.findall('Robocop eats baby food'))

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food'))

# Negative Character Classes

consonatsRegex = re.compile(r'[^aeiouAEIOU]') # This means not match these
print(consonatsRegex.findall('Robocop eats baby food.'))
