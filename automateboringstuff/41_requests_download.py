import requests 

target = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(target.raise_for_status())
print(target)

print(len(target.text))

# print(target.text)

playfile = open('RJtest.txt', 'wb')

for chunk in target.iter_content(100000):
    playfile.write(chunk)

playfile.close()
