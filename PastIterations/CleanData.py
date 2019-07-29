from moviepy.editor import *
import math

def clean(video, gpath):

    # Open up the file containing the gaze data using path given
    gazefile = open(gpath, "r")
    # Turn that file into a list with each line as an entry
    list_of_datapoints = gazefile.readlines()
    # The list of clips that we want to overlay on top of each other
    list_of_clips = []
    # How long the video is, and how we are going to keep track/record time (we are working backwards)
    running_time = video.duration

    # Loop that checks the most length of the timestamps. Another way to check the data
    # Still can be erroneous. Case of timestamp going from 9999 to 10000, etc.
    # modedict = {}
    # for i in range(0, entries):
    #     temp = len(list_of_datapoints[i].split()[2])
    #     if temp in modedict:
    #         modedict[temp] = modedict[temp] + 1
    #     else:
    #         modedict[temp] = 1
    #
    # maxnum = 0
    # maxval = 0
    # for i, j in modedict.items():
    #     if j > maxnum:
    #         maxnum = j
    #         maxval = i

    # Conditional gives us dimensions of computer to calibrate
    width = 1280
    height = 720

    # Calibration ratios
    # Width and height might need to be the resolution numbers that you used.
    x_ratio = (video.w - 20) / width
    y_ratio = (video.h - 20) / height

    # Where to start in these backwards for loops
    loop_end = len(list_of_datapoints) - 1

    # Backwards for loop so we don't have to adjust iterator variable when elements get removed
    # Scanning through the list and removing errors
    for i in range(loop_end, -1, -1):
        # Break each line to each individual entry
        line = list_of_datapoints[i]
        line = line.split()

        # If a line doesn't have three entries, remove it from the list
        if len(line) != 3:
            list_of_datapoints.pop(i)
            continue

        # This is the ending timestamp of the duration that was recorded of someone looking at that part of the screen
        end = float(line[2])

        # Remove the datapoint if the timestamp is zero or unusually high or low.
        if end / 1000000000 > 10 or end == 0: #or len(list_of_datapoints[i].split()[2]) != maxval:
            list_of_datapoints.pop(i)
            continue

        # Get the x and y coordinates from the line of data
        x = float(line[0]) * x_ratio
        y = float(line[1]) * y_ratio

        # If the coordinates aren't on the frame, remove it.
        if x > (video.w - 20) or x <= 0 or y > (video.h - 20) or y <= 0:
            list_of_datapoints.pop(i)

    # Update where the end of the loop is, now that the size of list_of_datapoints has changed
    loop_end = len(list_of_datapoints) - 1

    for i in range(loop_end, -1, -1):
        line = list_of_datapoints[i]
        line = line.split()

        # Only check for duration if we aren't looking at the last point, where we can't have a starting point for.
        if i != 0:
            # Getting to line above the one we got the coordinates from and denoting that timestamp as the "start"
            # timestamp of us looking at that location.
            top_line = list_of_datapoints[i - 1]
            top_line = top_line.split()
            start = float(top_line[2])
            end = float(line[2])
            # Find the duration with the start and end timestamps.
            duration = (end - start) / 1000

            # If the duration is negative, get rid of the top line because that means the top line happened after our
            # target line, which doesn't make sense and shouldn't happen.
            # Updates: the first two numbers algorithm didn't work because we found that the first two numbers can
            # change within a gaze data. Also, not every data timestamp starts in the billions.
            if duration < 0 or duration > video.duration / 2:
                list_of_datapoints.pop(i - 1)

    temp = [] 
    temp.insert(0, list_of_datapoints[0])
    not_repeat = True 
    for i in range(0, len(list_of_datapoints)): 
        for j in range(0, len(temp)): 
            if temp[j] == list_of_datapoints[i]: 
                not_repeat = False 
        if not_repeat: 
            temp.insert(len(temp), list_of_datapoints[i]) 
        not_repeat = True

    list_of_datapoints = temp

    f = open("cleaned_data.txt", "w+")
    for i in range(0, len(list_of_datapoints)):
        f.write(list_of_datapoints[i])
    f.close()