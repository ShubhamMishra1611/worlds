@echo off

git add .
set /p commit_message=Enter the commit message: 
git commit -m "%commit_message%"
git push -u origin main