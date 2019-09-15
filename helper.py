from moviepy.editor import *
import collections


def some_name(vpath, gpath, final_name):

    # Access the video using the path given
    video = VideoFileClip(vpath)
    # Open up the file containing the gaze data using path given
    gazefile = open(gpath, "r")
    # Turn that file into a list with each line as an entry
    list_of_datapoints = gazefile.readlines()
    # The list of clips that we want to overlay on top of each other
    list_of_clips = []
    # How long the video is, and how we are going to keep track/record time (we are working backwards)
    running_time = video.duration

    # Conditional gives us dimensions of computer to calibrate
    width = 1280
    height = 720

    # Calibration ratios
    # Width and height might need to be the resolution numbers that you used.
    x_ratio = (video.w - 20) / width
    y_ratio = (video.h - 20) / height

    cnt = collections.Counter()

    # Creates a counter that keeps track of how many copies of each line of datapoints there are in the dataset.
    for i in range(0, len(list_of_datapoints)):
        cnt[list_of_datapoints[i]] += 1

    # Gets rid of all but the first occurence of a repeated datapoint line
    for i in cnt.most_common():
        if i[1] > 1:
            counter = i[1]
            for j in range(len(list_of_datapoints) - 1, -1, -1):
                if list_of_datapoints[j] == i[0] and counter != 1:
                    list_of_datapoints.pop(j)
                    counter -= 1
                elif counter == 1:
                    break
        else:
            break

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
        if end / 1000000000 > 10 or end == 0:  # or len(list_of_datapoints[i].split()[2]) != maxval:
            list_of_datapoints.pop(i)
            continue

        # Get the x and y coordinates from the line of data
        x = float(line[0]) * x_ratio
        y = float(line[1]) * y_ratio

        # If the coordinates aren't on the frame, remove it. For some reason, the actual video width/length is not considered in the frame, but subtracting 20 does.
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

    # To write out the now cleaned list of datapoints 
    f = open(final_name + ".txt", "w+")
    for i in range(0, len(list_of_datapoints)):
        f.write(list_of_datapoints[i])
    f.close()

    # Update where the end of the loop is, now that the size of list_of_datapoints has changed
    loop_end = len(list_of_datapoints) - 1

    # Starting for loop for making the little clips of circles and putting it in a list.
    for i in range(loop_end, -1, -1):
        top_line = list_of_datapoints[i]
        top_line = top_line.split()

        start = float(top_line[2])

        x = float(top_line[0]) * x_ratio
        y = float(top_line[1]) * y_ratio

        # Only do this if we aren't looking at the end of the file, for it won't have an "ending" timestamp because it
        # is the last timestamp; we would normally compare the next timestamp to make the duration, but it doesn't
        # exist.
        if i != loop_end:
            line = list_of_datapoints[i + 1]
            line = line.split()
            end = float(line[2])
            duration = (end - start) / 1000
        else:
            # Have the last data point last for 10 milliseconds, since no "start" and "end" can be made for that point
            duration = 0.01

        # Create that clip of that circle using the data we got.
        shape = (ImageClip("shape.png")
                 .set_start(running_time - duration)
                 .set_end(running_time)
                 .set_duration(duration)
                 .set_pos((x, y)))

        # Update the running time, which represents the end timestamp of the next data point.
        running_time = running_time - duration

        # Insert that clip into the list that we are going to use to overlay all the clips on top of one another.
        list_of_clips.insert(0, shape)

    # Insert the actual video into the list.
    list_of_clips.insert(0, video)
    # Overlay the clips and make the video.
    final = CompositeVideoClip(list_of_clips)
    final.write_videofile(final_name + ".mp4")