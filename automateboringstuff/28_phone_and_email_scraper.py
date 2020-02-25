# TODO: Create a regex for phone numbers
# TODO: Create a regex for email addresses
# TODO: Get the text off the clipboard
# TODO: Extract the email/phone from this text
# TODO: Copy the extracted email/phone to the clipboard

import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(
    r'''
# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)        # first separator
\d\d\d        # first 3 digits
-        # separatoer
\d\d\d\d        # last 4 digits
(((ext(\.)?\s)|x)       # extension word-part (optional)
 (\d{2,5}))?   # extension the number part(a whitespace in the front of this line to make sure the most outside parens can work here)
)
''', re.VERBOSE
)  # Put everyting in one large group to make sure the findall can show it correctly, the biggest one will be group(0)

# TODO: Create a regex for email addresses
emailRegex = re.compile(
    r'''
# some.+_things@xxx.com

[a-zA-Z0-9_.+]+        # name part, in the [], for . + we don't need to \
@        # @ symbol
[a-zA-Z0-9_.+]+        # domain name part

''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()
# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedphone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedemail)
pyperclip.copy(results)
