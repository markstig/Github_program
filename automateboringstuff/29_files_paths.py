# \ on windows, / on mac and linux

print('\\')
print(r'c:\spam\eggs.png')

list = ['folder1', 'folder2', 'folder3']
print('\\'.join(list))

import os
print(os.path.join('folder1', 'folder2',
                   'eggs.png'))  # This will be use on windows/mac/linus

print(os.sep)
print(os.getcwd())
# os.chdir('c:\\')
print(os.getcwd())

print(os.path.abspath('spam.png'))
print(os.path.abspath('../../spam.png'))
print(os.path.isabs('../../spam.png'))  # check wether it is absolute path

print(os.path.relpath(
    '/folder1/folder2/spam.png',
    '/folder1'))  # given you the relative path between two given path

print(os.path.dirname('/folder1/folder2/folder3/spam.png')
      )  # this will retrieve the directory name of the file

print(
    os.path.basename('/folder1/folder2/folder3/spam.png')
)  # this will pull out the last part of the file path, both work on fiels and folders

print(os.path.exists('/folder1/folder2/folder3/folder4/spam/png')
      )  # check the file or folder exists or not

# check the path is a folder or file
os.path.isfile('/folder1/folder2/x.png')
os.path.isdir('/folder1/folder2')  # isdir or isfolder, try it.

# Get the size and the list of a particular dir
os.path.getsize('/folder1/folder2/folder3')
os.listdir('/foder1/folder2')

# makedir
# os.makedirs('/folder1/foder2')
