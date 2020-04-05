birthdays = {'Mark': '12-14', 'YAYA': '04-29'}

while True:
    print('Enter a name: (blank to quit)')
    name = input('name>>>> ')
    if name == '':
        break
    if name in birthdays:
        print(name + '\'s birthday is ' + birthdays[name])
    else:
        print('I don\'t have a birthday information for ' + name)
        print('What is his/her birthday information?')
        bday = input('Enter the birthday information>>>> ')
        birthdays[name] = bday
        print('Birthday database updated.')
        print(birthdays)
