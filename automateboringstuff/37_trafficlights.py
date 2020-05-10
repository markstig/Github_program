# assert False, 'This is the error message.'  # assert is just another kind of exception.

market_2nd = {'ns': 'green', 'ew': 'red'}


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
        # assert 'red' in intersection.values(), 'Neither light is red!!'
        if 'red' not in intersection.values():
            continue
        print(intersection)

for i in range(10):
    switchLights(market_2nd)


