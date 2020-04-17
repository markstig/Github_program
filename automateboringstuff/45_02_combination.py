import os, openpyxl

os.chdir('/users/markli/Downloads/')

wb = openpyxl.Workbook()

wb.save('testworkbook.xlsx')

workbook = openpyxl.load_workbook('testworkbook.xlsx')

print(type(workbook))

print(workbook.sheetnames)

sheet = workbook['Sheet']

print(sheet['A1'] == None)

sheet['A1'] = 'Names'
sheet['B1'] = 'Ages'

sheet2 = workbook.create_sheet(title = 'new sheet', index = 0)

for i in range(1, 10):
    sheet2.cell(row = i, column = 1).value = 100 + i

for i in range(1, 10):
    print(sheet2.cell(row = i, column = 1).value)

workbook.save('testworkbook.xlsx')

workbook.close()

print('All Done!!!')
