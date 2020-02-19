# Test 1
# spam = 0

# def eggs():
# spam = 1
# print(spam)

# eggs()

# Test 2
# def spam():
# eggs = 99
# bacon()
# print(eggs)

# def bacon():
# ham = 101
# eggs = 0

# spam()


# Test 3
def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)


eggs = 100
spam()
print(eggs)
