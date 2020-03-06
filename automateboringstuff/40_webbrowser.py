import webbrowser

address = input('Please enter your destination: ')

webbrowser.open('https://www.google.com/maps/place/' + address)


# Other 
import webbrowser, sys, pyperclip

# sys.argv # ['mapit.py', '870', 'Valencia', 'st.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # [combine the argumens to a string]
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
# https://www.google.com/maps/places/<address>
webbrowser.open('https://www.google.com/maps/places/' + address)

