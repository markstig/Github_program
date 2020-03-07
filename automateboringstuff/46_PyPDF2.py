# pip install PyPDF2

import PyPDF2
import os

os.chdir('c:\\Users\\Al\\documents')
pdfFile = open('meetingminutes1.pdf', 'rb')  # 'rb' stands for 'read binary' mode.

reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page = reader.getPage(0)
page.extractText()  # This will extract the texts from the page.

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
    
# Can't edit words in the pdfs.


import PyPDF2

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()  # Create a new PDF file. This file is in the RAM now.

for pageNum in range(reader1.numPages):  # Looping all the pages in reader1
    page = reader1.getPage(pageNum)  # Get each page
    writer.addPage(page)  # Add each page in 'writer'

for pageNum in range(reader2.numPages):  # Looping all the pages in reader2
    page = reader2.getPage(pageNum)  # Get each page
    writer.addPage(page)  # Add each page in 'writer'
    
outputFile = open('combineminutes.pdf', 'wb')  # Create a new PDF file. 

writer.write(outputFile)
pdf1File.close()
pdf2File.close()
outputFile.close()
