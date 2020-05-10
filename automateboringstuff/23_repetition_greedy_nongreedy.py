import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventure of Batman')
print(mo.group())

mo = batRegex.search('The advanture of Batwoman')
print(mo.group())

mo = batRegex.search('The advanture of Batwowowoman')
print(mo == None)  # No matched result, it will return None to mo

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('999-999-9999, call me.')
print(mo.group())
mo = phoneRegex.search('888-8888, call me.')
print(mo.group())

# If we wanted a regext object for the text "dinner?" (with the question mark), we should call this >>>> re.compile(r'dinner\?')

batRegex = re.compile(r'Bat(wo)*man')  # * means match 0 or more
batRegex = re.compile(r'Bat(wo)+man')  # + means match 1 + times

regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))

regex = re.compile(r'(\+\*\?)+')

haRegex = re.compile(r'(ha){3}')
print(haRegex.search('He said "hahaha"'))

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(
    phoneRegex.search('My numbers are 111-111-1111,222-222-2222,333-333-3333'))

haRegex = re.compile(r'(ha){3,5}')
print(haRegex.search('He said hahaha'))
print(haRegex.search('He said hahahaha'))
print(haRegex.search(
    'He said hahahahahaha'))  # still match but will only match the first 5 ha

digitRegex = re.compile(r'(\d){3,5}')
print(
    digitRegex.search('123456789')
)  # defaultly, python will do the greadymatches, it will match as long as possible

digitRegex = re.compile(
    r'(\d){3,5}?'
)  # This time it is non-greedymatch, this ? is not th same as before
print(digitRegex.search('123456789'))
