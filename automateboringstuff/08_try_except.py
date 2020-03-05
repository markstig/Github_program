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

# The second verson~
while True:
    try:
        enumerator = int(input('Please enter the enumerator: ')
        denominator = int(input('Please enter the denominator: ')
        result = enumerator / denominator
        print('The result is ' + str(result))
        continue1 = input('Continue or not? Y/N>>>> ')
        if continue1 == 'N':
            break
    except ZeroDivisonError:
        print('The denominator should not be 0')
    except ValueError:
        print('The input should be a number.')
