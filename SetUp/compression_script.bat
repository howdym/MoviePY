@echo off 
set /p start=What file do you want to reconfigure? (No file extension required)  
set /p end=What file do you want new one to be called? (No file extension required) 

ffmpeg -i %start%.avi inter.mp4 
del /f %start%.avi

move inter.mp4 %end%.mp4

set mydate=%date:~4,2%-%date:~7,2%-%date:~10,4%
mkdir %mydate%  
move 0* %mydate%