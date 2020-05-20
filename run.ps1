venv\Scripts\Activate.ps1
pyinstaller -F .\main.spec --icon=asserts/图标.ico
echo ''
echo ''
dist\main.exe