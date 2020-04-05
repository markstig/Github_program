# pw.py - An insecure password locker program.
import pyperclip, sys
PASSWORDS = {'google': 'testgoogle', 'facebook': 'testfacebook111', 'instagram': 'testins$'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [acount] - copy acount password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

print('---------------------------------')

if account in PASSWORDS:
    print('Here is the password: ' + pyperclip.paste())
