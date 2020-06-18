# checks a directory for a specific list of files
import os, time
import json
import requests
import datetime
import base64
import sys
from datetime import datetime, timedelta

print('Running RunIFP.py...')

#Read in configuration file
cwd = os.getcwd()
extractFileLocation = r'\\STAGING-ROKO-APPSERVER\InformentFiles\DATA'
achdate = datetime.today() - timedelta(days=1)

with open(os.path.join(cwd, 'ifp\\STAGING\\\mssql\FileCheck_config.json')) as f:
    config = json.load(f)
    #call API
    API_ENDPOINT = config['ServicingApi']
    importDate = achdate.strftime("%Y-%m-%d")
    payload = {
        'IsManual': 'false',
        'ImportDate': importDate,
        'CanImportTransactionTables': 'true',
        'CanImportHistoryTables': 'true',
        'CanTruncateTransactionTables': 'true',
        'CanTruncateHistoryTables': 'true',
        'CanImportStagingDatabase': 'true',
        'IsBackupRequired': 'true'
    }
    response = requests.post(url = API_ENDPOINT, data = payload)
    if response.text == 'true':
       # Remove all files
        files = os.listdir(extractFileLocation)
        for file in files:
           if (file.startswith("FF")):
                os.remove(os.path.join(extractFileLocation, file))
    else:
        sys.exit(13)
