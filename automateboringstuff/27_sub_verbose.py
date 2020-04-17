# The sub() Method, substitution

import re

namesRegex = re.compile(r'Agent \w+')
print(
    namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(
    namesRegex.sub('REDACTED',
                   'Agent Alice gave the secret documents to Agent Bob.'))

# Using \1, \2, etc in sub()
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent lice gave the secret documents to Agent Bob.'))
print(
    namesRegex.sub(r'Agent \1***',
                   'Agent Lice gave the secret documents to Agent Bob'))

# Verbose Mode with re.VERBOSE
re.compile(
    r'''
        (\d\d\d-)| # area code (without parens, with dash)
        (\(\d\d\d\)) # -or- area code with parens and no dasho
        \d\d\d # first 3 digits
        - # dash
        \d\d\d\d # last 4 digits
        ''', re.VERBOSE | re.DOTALL | re.IGNORECASE)

# Using Multiple Options (re.I, re.DOTALL, RE.VERBOSE)
