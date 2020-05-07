for i in range(4):
    print(i)

# Range objects and list-like values, range is list like
print(range(4))

# The list() Function, turn a range to a list value???
# print(list(range(4)))
# print(list(range(0, 100, 2)))

# an example
supplies = ['pens', 'staplers', 'flame-throwers', 'binder']
for i in range(len(supplies)):
    print(f"Index {i} in supplies is: {supplies[i]}")

# Multipe Assignment
cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

size, color, disposition = cat
print(size, color, disposition)

size, color, disposition = 'skinny', 'black', 'quiet'
print(size, color, disposition)

# Swapping Variables
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a)
print(b)

# Augmented assignment operators
spam = 0
spam = spam + 1  # spam += 1, += -= *= /= %=
