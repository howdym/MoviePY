@echo off

mkdir old_data
move 0* old_data

D:\python-3.7.4-amd64.exe

C:\Users\%username%\AppData\Local\Programs\Python\Python37\python.exe get-pip.py

C:\Users\%username%\AppData\Local\Programs\Python\Python37\Scripts\pip.exe install moviepy