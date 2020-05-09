import pandas as pd 
import os

# Set the target folder
targetfolder = r'C:\Users\mark.a.li\Downloads\tempfile'

for folder, subfolder, filename in os.walk(targetfolder):
    # Set an empty list first
    finallist = []
    for i in filename:
        targetfile = folder + '\\' + i
        # Define the area of the dataframe
        df = pd.read_excel(targetfile, skiprows=5, usecols='A:X')
        print('The {} has been loaded!!!'.format(i))
        # Add all the data frames to the list
        finallist.append(df)
# Concatenate the dataframes
finalpd = pd.concat(finallist, ignore_index = True)
print('Concatenate operation has been done!!!')
# Export to the targetfolder, and delete the default index
finalpd.to_excel(targetfolder + '\\' + 'finalfile.xlsx', index=False)
print('The new file has been created in {} folder!'.format(targetfolder))