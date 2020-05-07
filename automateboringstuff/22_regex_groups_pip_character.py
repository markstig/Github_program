import re
message = 'call me 333-333-3333, 555-555-5555 tomorrow'

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo)

# case2
message = 'my phone number is (666) 666-6666'
phoneNumberRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print(mo.group())

# | pipe character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile and batman is quite good.')
print(mo.group())

# case3
import pyperclip, pprint, re
message = pyperclip.paste()
sampleRegex = re.compile(r'((B|b)at(man|woman|mobile))')
print(sampleRegex.findall(message))
for i in sampleRegex.findall(message):
    print(i[0])
