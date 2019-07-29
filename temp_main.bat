@echo off

set /p vid=What video do you want to use? (no extension)
set /p gaze=What gazedata do you want to use? (add extension)

ffmpeg -i %vid%.avi %vid%.mp4
del /f %vid%.avi

:: Change this accordingly

set mydate=%date:~4,2%-%date:~7,2%-%date:~10,4%

move %vid%.mp4 %vid%-%mydate%.mp4

mkdir %mydate%

upload.bat

move 0* %mydate%

