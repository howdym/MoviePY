from moviepy.editor import *

def some_name():
    vpath = input("Type in video file name (with extension). ")
    gpath = input("Type in gaze file name. ")

    video = VideoFileClip(vpath)

    gazefile = open(gpath, "r")
    list_of_datapoints = gazefile.readlines()
    list_of_clips = []
    entries = len(list_of_datapoints)
    running_time = video.duration

    x_ratio = 720/1920
    y_ratio = 405/1080

    loop_end: int = entries - 1

    # TODO: Make a check for timestamp being in the millions or analyzes most often result

    for i in range(loop_end, -1, -1):
        #print("here")
        line = list_of_datapoints[i]
        line = line.split()

        if len(line) != 3:
            list_of_datapoints.pop(i)
            entries -= 1

        end = float(line[2])
        #print(end)

        x = float(line[0]) * x_ratio
        y = float(line[1]) * y_ratio

        if x >= 2000 or x <= 0 or y >= 2000 or y <= 0:
            list_of_datapoints.pop(i)
            entries -= 1
        
    #print(entries)
    #print(i)

        if i != 0:
            top_line = list_of_datapoints[i - 1]
            top_line = top_line.split()
            start = float(top_line[2])
            duration = (end - start) / 1000
        #print(duration)

            if duration < 0 or duration >= 7:
                #print(list_of_datapoints[i - 1])
                list_of_datapoints.pop(i - 1)
                entries -= 1

    # TODO: 516716640.000000

    loop_end = len(list_of_datapoints) - 1
    counter = 0

    for i in range(loop_end, -1, -1):

        if i != loop_end:
            line = list_of_datapoints[i + 1]
            line = line.split()

        top_line = list_of_datapoints[i]
        top_line = top_line.split()

        start = float(top_line[2])

        x = float(top_line[0]) * x_ratio
        y = float(top_line[1]) * y_ratio

        if i != loop_end:
            end = float(line[2])
            duration = (end - start) / 1000
        else:
            duration = 0.01

        if duration == 0:
            counter += 1
        else:
            duration -= 0.01 * counter
            counter = 0

        if counter != 0:
            duration = 0.01

        shape = (ImageClip("shape.png")
                 .set_start(running_time - duration)
                 .set_end(running_time)
                 .set_duration(duration)
                 .set_pos((x, y)))

        # shape = (ImageClip("shape.png")
        #          .set_start(running_time - duration)
        #          .set_end(running_time)
        #          .set_duration(duration)
        #          .set_pos((x, y)))

        #print("This is running time before change: ", running_time)

        running_time = running_time - duration

        list_of_clips.insert(0, shape)
        #print("This is running time after change: ", running_time)

        #print("This is raw x: ", float(top_line[0]))
        #print("This is raw y: ", float(top_line[1]))

    list_of_clips.insert(0, video)
    final = CompositeVideoClip(list_of_clips)
    final.write_videofile("test1.mp4")