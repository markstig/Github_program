# A Non-Regular Expression Example


def isPhoneNumber(text):  # 111-111-1111
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print(isPhoneNumber('hello'))
print(isPhoneNumber('111-111-2222'))

message = 'Call me 222-222-2222 tomorrow, or at 333-333-3333 for my office room'

foundNumber = False

for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not found any number.')

# The re Module
import re
message = 'call me 111-111-1111, or 999-999-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())
mo2 = phoneNumRegex.findall(message)
# print(mo2.group())  # List didn't have gourp() ?
print(mo2)
