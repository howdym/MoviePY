from moviepy.editor import *

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

line = None

for i in range(entries, 0, -1):

    if i != entries:
        line = list_of_datapoints[i]
        line = line.split()
        if len(line) != 3:
            continue

    top_line = list_of_datapoints[i - 1]
    top_line = top_line.split()

    if len(top_line) != 3:
        continue

    start = float(top_line[2])

    x = float(top_line[0]) * x_ratio
    y = float(top_line[1]) * y_ratio

    if i != entries:
        end = float(line[2])
        duration = start - end
    else:
        duration = 0.001

    if x >= 2000 or x <= 0 or y >= 2000 or y <= 0:
        running_time = running_time - 0.01
        continue

    if duration <= 0 or duration >= 0.02:
        duration = 0.010

    shape = (ImageClip("shape.png")
              .set_start(running_time - duration)
              .set_end(running_time)
              .set_duration(duration)
              .set_pos((x, y)))

    running_time = running_time - duration

    list_of_clips.insert(0, shape)

list_of_clips.insert(0, video)
final = CompositeVideoClip(list_of_clips)
final.write_videofile("test.mp4")