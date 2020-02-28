# A small check for important files before permanently delete them

import os, send2trash

# os.chdir('/users/markli')

print(os.listdir())

for filename in os.listdir():
    if filename.endswith('.py-'):
        # os.unlink(filename)  # check before run this script
        print(filename)

send2trash.send2trash('/users/markli/Downloads/test.txt')  # delete the files to the recycle bin
