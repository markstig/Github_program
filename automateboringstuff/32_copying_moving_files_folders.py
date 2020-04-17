import shutil, os

# os.mkdir('/users/markli/Downloads/shutil')

# shutil.copy('/users/markli/Downloads/test.txt', '/users/markli/downloads/shutil/')

# shutil.copy('/users/markli/Downloads/test.txt', '/users/markli/downloads/shutil/renametest.txt')  # copy and rename

# shutil.copytree('/users/markli/downloads/', '/users/markli/Downloads/shutil/') # Copy the whole folders and files inside it

# shutil.move('/users/markli/Downloads//test.txt', '/users/markli/Downloads/shutil/')
# shutil.move('/users/markli/Downloads//test.txt', '/users/markli/Downloads/shutil/rename2txt.txt') # No shutile.rename function, but we can use this

# Deleting files

# os.unlink('/users/markli/Downloads/test.txt') # permanently delete this file
# os.rmdir('/users/markli/Downloads/shutil') # delete folder, if the folder has files, it will show a warnig.
shutil.rmtree(
    '/users/markli/Downloads/shutil'
)  # delete the folder and the files in it. permanently delete, not in the recycle bin

print('Done!!!')
