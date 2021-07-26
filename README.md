# Kismet-to-Wigle-CSV
## Short Python Script to convert .kismet files to Wigle CSV then Upload to Wigle

Uses the kismetdb cli tool to convert the .kismet log files from Kismet to a Wigle CSV file 

The script will convert all kismet files then ask if you want to upload those to Wigle

## Usage 
Place the script in the same directory as the .kismet files

Enter your API token which can be found at https://wigle.net/account

Then run the script...

sudo python3 Kismet_To_CSV.py

The sctipt finds all .kismet files and systematically converts then to CSV files

If you entered yes to the upload question it will then upload your files to your wigle account
