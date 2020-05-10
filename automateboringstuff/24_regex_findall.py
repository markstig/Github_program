import re

resume = '''
phone number 111-111-1111
phone number 222-222-2222
'''

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.search(resume))
print(phoneRegex.findall(resume))

# search returns match objects, findall returns a list of strings

# This is the behavior for regex objects that have ZERO or ONE groups in them.

# Has two or more groups = list of tuples of strings
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(resume))

phoneRegex = re.compile(
    r'((\d\d\d)-(\d\d\d-\d\d\d\d))')  # Here are three groups
print(phoneRegex.findall(resume))
