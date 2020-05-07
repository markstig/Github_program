# use + to concatenate strings
print('Hello' + 'World!')

name = 'Mark'
place = 'Shanghai'
time = '6 pm'
food = 'turnips'
print('hello ' + name + ', you are invited to a party at ' + place + ' at ' +
      time + '. Please bring ' + food + '.')

# String Formatting %s - conversion specifiers
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' %
      (name, place, time, food))
