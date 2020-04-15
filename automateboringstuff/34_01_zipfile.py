import zipfile, os

os.chdir('/users/markli/downloads/')

examplezip = zipfile.ZipFile('Archive.zip') # Archive.zip is an existing zip file

print(examplezip.namelist())

spaminfo = examplezip.getinfo('chromedriver')
print(spaminfo.file_size)
print(spaminfo.compress_size)

print('Compressed file is %sx smaller!'%(round(spaminfo.file_size/spaminfo.compress_size, 2)))
examplezip.close()

# examplezip.extractall()
# examplezip.extract('chromedrive', 'pathB')

# newzip = zipfile.ZipFile('new.zip', 'w')
# newzip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newzip.close()
