import os

helloFile = open('/users/markli/Downloads/test.txt', 'w')
helloFile.write('This is a test line.')
helloFile.write('\nThis is a second line.')
helloFile.close()

helloFile = open('/users/markli//Downloads/test.txt')
# print(helloFile.read())
print('>>>>>>>>>>>>>>>>')
print(helloFile.readline())
print(helloFile.readline())
helloFile.close()

helloFile = open('/users/markli/Downloads/test.txt', 'a')
helloFile.write('This is an append line.')
helloFile.close()

print('>>>>>>>>>>>>>>>>')
helloFile = open('/users/markli//Downloads/test.txt')
print(helloFile.readlines())
