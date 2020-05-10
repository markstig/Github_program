import win32com.client as win32
import os

def trans(fullfilename):
    fname = fullfilename
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = excel.Workbooks.Open(fname)

    wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
    wb.Close()                               #FileFormat = 56 is for .xls extension
    excel.Application.Quit()

targetpath = r'C:\Users\mark.a.li\Downloads\tempfile'

for folder, subfolder, filename in os.walk(targetpath):
    for i in filename:
        fullfilename = folder + '\\' +i
        trans(fullfilename)
        print(i + 'has been transformed already!!!')

