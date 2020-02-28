import os, shutil

print(os.walk('/users/markli/OneDrive/temp/'))

for foldername, subfolders, filenames in os.walk(
        '/users/markli/OneDrive/temp/'):
    print('The folder is: ' + foldername)  # foldername is one foldername
    print('The subfolders in ' + foldername + ' are ' +
          str(subfolders))  # subfolders will be a list
    print('The filenames in ' + foldername + ' are ' + str(filenames))
    print('Done!!!')

    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)
        else:
            print('>>>>>>>>>No fish folder!')
    for file in filenames:
        if file.endswith('.pdf'):
            print('Find the pdf file --- ' + file)
    # for file in filenames:
    # if file.endswith('.py'):
    # shutil.copy(os.join(foldername, file), os.join(foldername, file + '.backup'))
