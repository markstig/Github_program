import os

print(os.getcwd())
pathstring = '/Users/markli/OneDrive/Study/temp/markpython/prog_study/automateboringstuff/'
totalSize = 0
for filename in os.listdir(pathstring):
    if not os.path.isfile(os.path.join(pathstring, filename)):
        print(filename)
        continue
    print(filename + '>>>' + 'the size of the file is', os.path.getsize(os.path.join(pathstring, filename)))
    totalSize = totalSize + os.path.getsize(os.path.join(pathstring, filename))
    print('right now the total size is: ', totalSize)

print(totalSize)

# the second way to make this
import os
print(os.getcwd())
os.chdir('xxxx')
print(os.getcwd())

size = 0
for i in os.listdir():
    if os.path.isfile(i):
        filesize = os.path.getsize(i)
        size = size + os.path.getsize(i)
        print(f'the filename is {i}, the filesize is {filesize}, the totalsize is {size}')
