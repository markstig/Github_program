def factorial(f):
    if f < 2:
        return 1
    # Here we must use return to get the value, because we can't concatenate the int and function directly.
    return f * factorial(f-1)

def sums(s):
    if s < 1:
        return 0
    return s + sums(s-1)

while True:
    number = int(input('Please input the number>>> '))
    fnumber = factorial(number)
    snumber = sums(number)
    print('The factorial number is: ', fnumber)
    print('The sum number is: ', snumber)
