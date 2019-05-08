#Code credited:
#https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py

#Import Dependencies 
import os
import glob
import pandas as pd
os.chdir("CSV files")

#Use glob to pattern match 'csv'
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_bike_data.csv", index=False, encoding='utf-8-sig')