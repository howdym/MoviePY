import iteration4
import test
import sys
from moviepy.editor import *
import CleanData
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import math
import time

# Sample cmd using main: python main.py [Video file] [Gaze data file] [Computer type (MC or Posyx = 1, DYN = 2)]
# iteration3.some_name(sys.argv[1], sys.argv[2], int(sys.argv[3]))
iteration4.some_name(sys.argv[1], sys.argv[2], sys.argv[3])
# test.some_name(sys.argv[1])

# video = VideoFileClip(sys.argv[1])
#
# running_time = video.duration
#
# CleanData.clean(video, sys.argv[2])
#
# gazefile = open("cleaned_data.txt", "r")
#
# list_of_datapoints = gazefile.readlines()
#
# list_of_clips = []
#
# entries = len(list_of_datapoints)
#
# clipnum = 1
#
# a = 0
# gazename = "gaze" + str(clipnum) + ".txt"
# f = open(gazename, "w+")
#
# start = 0
# end = 0
#
# first = float(list_of_datapoints[0].split()[2])
# last = 0
# while a < entries:
#     if first + clipnum * 250000 < float(list_of_datapoints[a].split()[2]):
#         last = float(list_of_datapoints[a - 1].split()[2])
#         end = start + (last - first)
#         first = last
#         f.close()
#         f = None
#         temp = video.subclip(start / 1000, end / 1000)
#         iteration4.some_name(temp, gazename, int(sys.argv[3]), clipnum)
#         start = end
#         clipnum += 1
#         gazename = "gaze" + str(clipnum) + ".txt"
#         f = open(gazename, "w+")
#         f.write(list_of_datapoints[a])
#     elif a == entries - 1:
#         f.write(list_of_datapoints[a])
#         f.close()
#         end = video.duration
#         temp = video.subclip(start, end)
#         iteration4.some_name(temp, gazename, int(sys.argv[3]), clipnum)
#         clipnum += 1
#     else:
#         f.write(list_of_datapoints[a])
#     a += 1
#
# list_of_videos = []
# for i in range(1, clipnum):
#     vname = "video" + str(i) + ".mp4"
#     list_of_videos.insert(0, VideoFileClip(vname))
# final_clip = concatenate_videoclips(list_of_videos)
# final_clip.write_videofile("final.mp4")
#
