import re

def check_aei(text):
    result = re.search(r'a\we\wi', text)
    return result != None

print(check_aei('academia'))
print(check_aei('aerial'))
print(check_aei('paramedic'))
