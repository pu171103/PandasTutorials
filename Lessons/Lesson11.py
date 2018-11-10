###############################################################################
###  Pandas Tutorials - Lesson 11                                           ###
###############################################################################

import matplotlib
import os
import sys
import pandas as pd

# Create 3 Excel Files
d = {'Channel':[1], 'Number':[255]}
df = pd.DataFrame(d)

df.to_excel('test1.xlsx', sheet_name='test1', index=False)
df.to_excel('test2.xlsx', sheet_name='test2', index=False)
df.to_excel('test3.xlsx', sheet_name='test3', index=False)

# Put all Excel files into one dataframe
# Wildcard search for files ending in 'xlsx'
FileNames = []
for files in os.listdir():
    if files.endswith('.xlsx'):
        FileNames.append(files)

# Create a convenience function to process the files
def GetFile(fnombre):
    location = os.getcwd() + '\\' + fnombre

    # Parse the file (0 = first sheet)
    df = pd.read_excel(location, 0)

    # Tag record to file name
    df['File'] = fnombre

    # Make the "File" column the index of the dataframe
    return df.set_index(['File'])

# Create a list of dataframes 
df_list = [GetFile(fname) for fname in FileNames]

# Combine the dataframes into one dataframe
big_df = pd.concat(df_list)
