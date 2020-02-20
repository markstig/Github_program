# Lists of lists

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[0][-1])

# Slices, index = Single Value, Slice = list of Values

print(spam[1][1:3])

# Change a List's Items

spam = [10, 20, 30]
spam[1] = 'Hello'
print(spam)
spam[1:3] = [
    'CAT', 'DOG', 'MOUSE'
]  # pay attention [1:3] only including 2 items here, but we added 3 items.
print(spam)

# Slice shortcut
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])
# Delete use the del Satament, this del Statement = 'Unassignment' statement
del spam[2]
print(spam)

# String and List Similarities
print(len('Hello'))
print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5.6])
print([1, 2, 3] * 3)

# The list() function
print(int('42'))
print(str(42))
print(list('Hello'))

# The in and not in Operators
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print('howdy' not in ['hello', 'hi', 'howdy', 'heyas'])
