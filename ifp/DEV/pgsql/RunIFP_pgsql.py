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
extractFileLocation = r'\\vm-roko-appserver\CascadeFinancials\Cobol\CobolTempDirectory\PGSQL'
DateFormat = "%Y-%m-%d"
achdate = datetime.today() # - timedelta(days=1)
IsManual = 'false'

importDate = achdate.strftime(DateFormat)

with open(os.path.join(cwd, 'ifp\\DEV\\\pgsql\FileCheck_config.json')) as f:
    config = json.load(f)
    #call API
    API_ENDPOINT = config['ServicingApi']
    #OverwriteImportDate =  os.getenv("OverwriteImportDate")
    
    #if OverwriteImportDate == "1900-01-01": # or OverwriteImportDate is None:
    #    importDate = achdate.strftime(DateFormat)
    #else:
    #    importDate = datetime.strptime(OverwriteImportDate, DateFormat).strftime(DateFormat)
                
    payload = {
        'IsManual': IsManual,
        'ImportDate': importDate,
        'CanImportTransactionTables': 'true',
        'CanImportHistoryTables': 'true',
        'CanTruncateTransactionTables': 'true',
        'CanTruncateHistoryTables': 'true',
        'CanImportStagingDatabase': 'true',
        'IsBackupRequired': 'true'
    }
    print (payload)
    
#    response = requests.post(url = API_ENDPOINT, data = payload)
#    if response.text == 'true':
#       # Remove all files
#        files = os.listdir(extractFileLocation)
#       for file in files:
#            if (file.startswith("FF")):
#                os.remove(os.path.join(extractFileLocation, file))
#    else:
#        sys.exit(13)
