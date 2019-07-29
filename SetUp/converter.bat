@echo off

set /p vid=What video do you want to use? (no extension)
set /p gaze=What gazedata do you want to use? (add extension)

ffmpeg -i %vid%.avi %vid%.mp4
del /f %vid%.avi

:: Change this accordingly

python main.py %vid%.mp4 %gaze%

move %vid%.mp4 old_data 
