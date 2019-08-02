from moviepy.editor import *
import os

directory_start = "./"
list_of_sessions = []
list_of_folders = []

for x in os.walk(directory_start):
    if x[0][len(x[0]) - 4: len(x[0])] == "2019":
        list_of_sessions.append(os.path.join(x[0], "ssi"))

for f in list_of_sessions:
    for i in os.walk(f):
        if len(os.listdir(i[0])) <= 8 and i[0] != f:
            list_of_folders.append(i[0])
    for i in list_of_folders:
        gaze = ""
        video = ""
        audio = ""
        for filename in os.listdir(i):
            if filename.endswith(".stream~") or filename.endswith(".stream_"):
                gaze = filename
            elif filename.endswith(".mp4") or filename.endswith(".avi"):
                video = filename
            elif filename.endswith(".wav"):
                audio = filename
        last_fslash = i.rfind('\\')
        first_bslash = i.find('/')
        comp_name = i[last_fslash + 1: len(i)]
        sesh_number = i[first_bslash + 1: first_bslash + 10]
        name = sesh_number + comp_name + "_overlayed"
        clip = VideoFileClip(video)
        if float(clip.w / clip.h) != float(1280 / 720):
            os.system("ffmpeg -i" + video + "-vf scale=720:405 inter1.mp4")
            os.system("del /f " + video)
            os.system("move inter1.mp4" + video)
        # os.system("ffmpeg -i " + video " -i " + audio + " -codec copy -shortest inter.mp4")
        # os.system("python main.py inter.mp4 " + gaze + name)
        # os.system("del /f inter.mp4")
    list_of_folders.clear()
