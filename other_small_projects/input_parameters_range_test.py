def getrange():
    a = input('Please input a: ')
    if a != '':
        a = int(a)
    b = input('Please input b: ')
    if b != '':
        b = int(b)
    c = input('Please input c: ')
    if c != '':
        c = int(c)

    if a == '' and c == '':
        return range(b)
    elif c == '':
        return range(a, b)
    else:
        return range(a, b, c)
    raise Exception('b should at least be an integer except 0.')

def printrange(x):
    print('The current range is: ', x)
    for i in x:
        print(i)

while True:
    printrange(getrange())