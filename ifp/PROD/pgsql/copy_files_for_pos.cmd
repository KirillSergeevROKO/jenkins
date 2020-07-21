@echo on
::Scripts for copy COBOL files for MSSQL  for task DEV-1933 
:: Written by: Kirill Sergeev / Kirill.Sergeev@rokolabs.com
:: Version 1.0.1   03.26.2020

:: example
:: "Copy_files_for_pos.bat \\testhost1\source_folder \\testhost2\destination_folder"


set "SOURCE=%1"
set "DEST=%2"

::Set date format YYYYDDMM for BACKUP folders 
set DATE_FORMAT=%date:~10,4%%date:~4,2%%date:~7,2%

::Check parameters 
IF '%1'=='' (
    echo "Please set path to your SOURCE folder!!!"
    echo.
    echo "Copy_files_for_pos.bat [SOURCE path] [DESTINATION path]"
    echo "Example:"
    echo "Copy_files_for_pos.bat \\testhost1\source_folder \\testhost2\destination_folder "
    echo.
    EXIT /B 1
    
)

IF '%2'=='' (
    echo "Please set path to your DESTINATION folder!!!"
    echo.
    echo "Copy_files_for_pos.bat [SOURCE path] [DESTINATION path]"
    echo "Example:"
    echo "Copy_files_for_pos.bat \\testhost1\source_folder \\testhost2\destination_folder "
    echo.
    EXIT /B 1
)

::Set folders path -  parameter+date
set "SOURCE_PATH=%SOURCE%\%DATE_FORMAT%\Backup"
set "DEST_PSSQL=%DEST%\"


::Check folders exist 
IF NOT EXIST %SOURCE_PATH% (
    echo "%SOURCE_PATH% folder doesn't exists!! Please check SOURCE folder"
    EXIT /B 1 
)

IF NOT EXIST %DEST_PSSQL% (
    echo "%DEST_PSSQ% folder doesn't exists!! Please check DESTINATION folder"
    EXIT /B 1 
)

:: Clear DESTINATION folder 
echo "Clear DEST folder"
del "%DEST_PSSQL%\*" /f /q


::Copy files from SOURCE_PATH to DEST_PSSQL
echo "Copy files to Postgress folder"

robocopy %SOURCE_PATH% %DEST_PSSQL% 

::Copy file from errors folder if it exist 
IF EXIST %SOURCE_PATH%\errors (
    echo "Copy files from errors folder"
    robocopy %SOURCE_PATH%\errors\ %DEST_PSSQL%
)

::Convert file FFSI000A1 to FFSI000A and remove FFSI000A2

del "%DEST_PSSQL%\FFSI000A2"
ren "%DEST_PSSQL%\FFSI000A1" "FFSI000A"

:: Delete specific files

del "%DEST_PSSQL%\FFSI055A