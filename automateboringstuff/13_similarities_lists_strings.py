print(list('hello'))

name = 'Zophie'
print(name[0])
print(name[1:3])
print(name[-2])
print('Zo' in name)
print('xxx' in name)

for letter in name:
    print(letter)

# Mutable(list) and Immutable(string) Data Type, a string can not be changed

# Creating New String from slices
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# The difference between immutable and mutable comes up with "references", explained next.
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

spam = [
    0, 1, 2, 3, 4, 5
]  # python assigned a reference to this list, this is why it can be changed even if we didn't change spam directly.
# Immutable values don't have this problem because they can't be modified "in place". They can only be replaced by new values.
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)


# Passing Lists in Function Calls...
def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
newSpam = eggs(spam)
print(spam)

# The copy.deepcopy() Function
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(
    spam)  # It copied a brand new list based on the spam list.
cheese[1] = 42
print(cheese)
print(spam)

# Line Constinuation, python will ignor the indentation in the following conditions.
spam = ['apples', 'orranges', 'bananas', 'cats']
print(spam)

print('Four score and seven' + \
        'years ago.')
