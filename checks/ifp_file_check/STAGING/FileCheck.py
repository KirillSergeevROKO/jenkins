# checks a directory for a specific list of files
import os, time
import json
import requests
import datetime
import smtplib
import base64
import glob
import sys
from datetime import datetime, timedelta
from email.mime.text import MIMEText

print('Running FileCheck.py...')
def sendEmail(sendTo, user, password):
    s = smtplib.SMTP(host='smtp.office365.com', port='25')
    s.starttls()
    s.login(user, password)
    
    body = "Informent Files are missing from FTP transfer"
    msg = MIMEText(body)
    msg['Subject'] = "Informent File Check"
    msg['To'] = sendTo
    msg['From'] = user

    s.send_message(msg)
    s.close()

#Read in configuration file
cwd = os.getcwd()
with open(os.path.join(cwd, 'checks\\ifp_file_check\\STAGING\\FileCheck_config.json')) as f:
    config = json.load(f)

sleepTime = config['SleepTime']
totalRetryTime = config['TotalRetryTime']
sendToAddress = config['Email']['SEND_TO']
accountName = config['Email']['USERNAME']
accountPassword = config['Email']['PASSWORD']

accountPassword = base64.b64decode(accountPassword)
accountPassword = accountPassword.decode('UTF-8')

achdate = datetime.today() - timedelta(days=1)
formated_date = achdate.strftime("%Y%m%d")
informentDirectory = config['Informent']['Directory']
informentDirectory_error = str(informentDirectory) + "\\errors"

print(informentDirectory)
print(informentDirectory_error)
#prepend directory to file names
filelist = [f'{informentDirectory}\\{file}' for file in config['Informent']['FileNames']]
# add ach file to list as name changes
#achdate = datetime.today() # - timedelta(days=1)
#achFileMask = f'ach618.{achdate:%Y%m%d}*.txt'


while True:
    if all([os.path.isfile(f) for f in filelist]) and glob.glob(os.path.join(informentDirectory)) :
        print('All files are present')
        break
    else :
        print('Not all files found.')
        if(totalRetryTime <= 0):
            print('Sending failure email...')
            #sendEmail(sendToAddress, accountName, accountPassword)
            sys.exit(2)
        else:
            # sleep
            print(f'Sleeping for {sleepTime} seconds')
            totalRetryTime -= sleepTime
            print(f'Total Retry Time Remaining : {totalRetryTime} seconds')
            time.sleep(sleepTime)
            