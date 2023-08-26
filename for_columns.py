# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:08:07 2023

@author: Shubham Jaiswal
"""
import os
import pandas as pd

folder_path = r'C:\Users\Shubham Jaiswal\Desktop\Mtech_Project_Results\columns'
d={}
l=[]
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(filename)
        #print(file_path)
        with open(file_path, 'r') as f:
            next(f) # skip the first line
            for line in f:
                value = line.split()[1]
                l.append(float(value))
            d[file_path[50:-4]]=l
            l=[]

# Create a pandas dataframe from the dictionary
df = pd.DataFrame(d)

# Create a Pandas Excel writer using xlsxwriter as the engine
writer = pd.ExcelWriter('column.xlsx', engine='xlsxwriter')

# Write the dataframe to a sheet named 'Sheet1'
df.to_excel(writer, sheet_name='Sheet1')

# Save the Excel file
writer.save()                          
      
