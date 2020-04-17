import re

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))

endsWithWorldRegex = re.compile(r'$World!')
print(endsWithWorldRegex.search('Hello World!'))  # ??? why return None ???

# ^both$ means pattern must match the entire string
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('1213123123hel'))

# . anything except newline
atRegex = re.compile(r'.at')  # anything followed an at
print(atRegex.search('The cat in the hat sat on the flat mat.'))

names = 'First Name: Al Last Name: Swegart'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(names))

#(.*) is greedy, (.*?) is non-greedy
serve = '<To serve humans> for dinner>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<.*>')
print(greedy.findall(serve))

# Making Dot Match Newlines Too (with re.DOTALL)

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))

dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(
    vowelRegex.findall(
        'Al, why does your programming book talk about RoboCop so much?'))

vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)  # We can use I for short
print(
    vowelRegex.findall(
        'Al, why does your programming book talk about RoboCop so much?'))
