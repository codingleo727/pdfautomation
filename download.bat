@ECHO OFF
FOR /F "USEBACKQ TOKENS=2,*" %%a IN (
    `REG QUERY "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /V {374DE290-123F-4565-9164-39C4925E467B}`
) DO (
    SET DOWNLOADS=%%b
)
ECHO %DOWNLOADS% > downloads_folder.txt