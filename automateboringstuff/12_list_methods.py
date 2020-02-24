# The index() list medthod

spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

# The append(), insert(), and remove() list methods
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam.insert(1, 'chicken')
print(spam)

spam.remove('bat')
del spam[0]
print(spam)

# The sort() list method, cannot sort the numbers and strings at the same time
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = ['ants', 'Cats', 'dogs', 'badgers',
        'elephants']  # Uppercase comes first!!!
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)
