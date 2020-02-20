while True:
    enumerator = input('Please enter the enumerator: ')
    denominator = input('Please enter the denominator: ')

    try:
        enumerator = int(enumerator)
        denominator = int(denominator)
        print(enumerator/denominator)
    except ZeroDivisionError:
        print('Error: You tried to divided by zero')
    except ValueError:
        print('Error: You did not enter a number')
