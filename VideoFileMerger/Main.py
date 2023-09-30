from moviepy.editor import *
import os

def concatenate():
    file_list = os.listdir(path="E:/Projects/Code/Projects/VideoFileMerger/Input")
    file_path_list = []
    for file in file_list:
        file_path_list.append(f"Input/{file}")
    clips = [VideoFileClip(c) for c in file_path_list]
    merged_clip = concatenate_videoclips(clips, method="compose")
    merged_clip.write_videofile("E:/Projects/Code/Projects/VideoFileMerger/Output/new.mp4")

concatenate()