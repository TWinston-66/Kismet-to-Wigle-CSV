########### Kismet to Wigle CSV Conversion Scipt ###########

import os 
import pathlib
import requests

# Define path of .kismet files
path = pathlib.Path(__file__).parent.resolve()
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

# Upload CSV Files to Wigle
def upload_files():
    url = 'https://api.wigle.net/api/v2/file/upload' 
    path = pathlib.Path(__file__).parent.resolve()
    files = os.listdir(path)

    x = 0
    csv = []
    for file in files:
        length = len(file)
        len1 = length - 4
        ext = file[len1:length]
        if ext == '.csv':
            csv.append(file)

    Total = len(csv)

    for file_csv in csv:
        x = x + 1
        data = {'file': (file_csv, open(file_csv, 'rb'), 'multipart/form-data', {'Expires': '0'})}
        print(str(x) + '/' + str(Total))
        print('Uploading *' + file_csv + '*')
        r = requests.post(url, files = data, headers = {'Authorization': 'Basic YOUR API TOKEN HERE'})
        status = r.status_code
        if status == 200:
            print('Done!' + '\n')
        elif status != 200:
            print('Failed...')
            print('Status Code: ' + str(status) + '\n')

def ask_upload():
    upload = input('Upload CSVs to Wigle?(y/n)')

    if upload == 'Y' or upload == 'N':
        print('\n' + 'Please enter y or n')
        ask_upload()
    elif upload == 'y':
        upload_files()
    return upload

ask_upload()
