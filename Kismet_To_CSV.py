########### Kismet to Wigle CSV Conversion Scipt ###########

import os 

# Define path of .kismet files
path = "/home/winston/Documents/Wardriving"
files = os.listdir(path)

# Define .kismet file list
Kismet = []

# Append all .kismet files to list 
for file in files:
    length = len(file)
    len1 = length - 7
    ext = file[len1:length]
    if ext == '.kismet':
        Kismet.append(file)

total = len(Kismet)
i = 0 

# Convert Kismet to Wigle CSV
for kis in Kismet:
    i = i + 1
    command = 'kismetdb_to_wiglecsv --in ' + kis + ' --out ' + kis[0:len(kis) - 7] + '.csv'
    print(str(i) + '/' + str(total))
    print("Converting *" + kis + '*')
    os.system(command)
    print('Done!' + '\n')