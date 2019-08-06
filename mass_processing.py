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
        temp_name = ""
        temp_name2 = ""
        for filename in os.listdir(i):
            if filename.endswith(".stream~") or filename.endswith(".stream_"):
                gaze = os.path.join(i, filename)
            elif filename.endswith(".mp4") or filename.endswith(".avi"):
                video = os.path.join(i, filename)
            elif filename.endswith(".wav"):
                audio = os.path.join(i, filename)
            temp_name = os.path.join(i, "inter.mp4")
            temp_name2 = os.path.join(i, "inter1.mp4")
        last_fslash = i.rfind('\\')
        first_bslash = i.find('/')
        comp_name = i[last_fslash + 1: len(i)]
        sesh_number = i[first_bslash + 1: first_bslash + 10]
        name = sesh_number + comp_name + "_overlayed"
        clip = VideoFileClip(video)
        if float(clip.w / clip.h) != float(1280 / 720):
            os.system("ffmpeg -i " + video + " -vf scale=720:405 " + temp_name2)
            video = temp_name2
        os.system("ffmpeg -i " + video + " -i " + audio + " -c:a aac -shortest " + temp_name)
        os.system("python main.py " + temp_name[2:len(temp_name)] + " " + gaze[2:len(gaze)] + " " + name)
        os.system("del /f " + temp_name[2:len(temp_name)])
        if temp_name2 == video:
            os.system("del /f " + temp_name2[2:len(temp_name2)])
    list_of_folders.clear()
