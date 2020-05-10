# """

# ******************
# *                *
# *                *
# *                *
# ******************

# """


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol must be a string of the length 1')
    if (width < 2) or (height<2):
        raise Exception('Width and height must >=2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol + ' '*(width-2) + symbol)
    print(symbol*width)

boxPrint('*', 20, 5)


# How  to print a triangle ????
