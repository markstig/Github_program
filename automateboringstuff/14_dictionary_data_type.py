myCat = {'size': 'fat', 'color': 'gray', 'dispositon': 'loud'}
print(myCat['size'])
print('My cat has' + myCat['color'] + 'fur.')
spam = {12345: 'Luggage combination', 45: 'The answer'}
print(spam)

# Dictionaries are unordered
print([1, 2, 3] == [3, 2, 1])  # This is different with list

# Check the dictionary with the in and not in
print('size' in myCat)

# The keys(), values(), and items() Dictionary Methods

print(list(myCat.keys()))
print(list(myCat.values()))
print(myCat.items())

for k in myCat.keys():
    print(k)

for k, v in myCat.items():
    print(k, v)

for i in myCat.items():
    print(i)

# The get() can check the values and give another result if no such value
picnicItems = {'apples': 5, 'cus': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic')

# The setdefault() Dictionary Method
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
if 'color' not in eggs:
    eggs['color'] = 'black'
print(eggs)

eggs.setdefault('teeth', 'white')
print(eggs)
