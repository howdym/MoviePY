This repository contains scripts that was used to clean and filter the gaze data taken from students when they were on their laptops for TIILT's study on Coding with Minecraft. The gaze data is then overlayed onto the corresponding screen captures of the students.

UPDATES:
1. There turned out to be a delay, or some misrepresentation of time in the gazedata and the video. So, we are back to working with the idea of working backwards and seeing where it goes.

2. Data repeats. The script now parses through the data and eliminates repetition. Makes the script a bit slower.

NOTE: This system is specifically made for the data from the SSI pipelines that were taken from TIILT's study on Coding with Minecraft. So, if you're just trying to put some random data into this script, no guarantee it will work. 

CONTENTS: 

mass_processing.py: This is the script I made to automate the process of filtering the data of each student's videos. We had each of their videos and their corresponding gaze data in seperate folders, so the script scrapes through each folder and processes the data automatically. 

main.py: This is the script to run when you want to process one set of data. Further instructions are in the comments of that script. 

helper.py: This is the script that contains the body of the main function. This is where the data is processed, overlayed, etc. The rationale between the seperation of the helper and main script was because it was easier to make Windows Batch Files to automate testing and execute os commands within the Python script. 

shape.png: The circle that represents the gaze data that gets overlayed onto the screen recording. In other words, where the circle is on the screen recording is where the student is looking. 

reformat.bat: When we initially collected the data from the students, we first uploaded them onto Box. It was quite a tedious process because we also needed to reformat the video extension and resolution sometimes, and this script automates that process. Parts of this script (not the uploading) were used in practice.

upload.bat/upload.py: The scripts that upload the files onto Box. Was never actually used in practice because we were done collecting data soon after this script was done being written. 

SetUp: This folder contains the scripts that helped automate other miscellaneous processes. Not actually much of a significant contribution to the main purpose of this repository, but keeping it here in case it ever comes to use. 

PastIterations: Past iterations of the processing script (helper.py).