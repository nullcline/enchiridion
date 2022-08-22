
import cv2
import numpy as np
from glob import glob
import os
import sys
'''
Checks every folder in flight_data for a video file, and
generates a video if there isn't one in the folde

If you run this on linux make sure to have run:
$ sudo apt-get install ffmpeg x264 libx264-dev

generates a video if there isn't one in the folder
'''

# jump back one
sys.path.insert(0, r"../")

img_array = []
flight_folders = glob("flight_data/*/", recursive = True)

for folder in flight_folders:

    # check if theres a .mp4
    try:
        if not any(".mp4" in file for file in os.listdir(folder)):
            frames = len(os.listdir(folder))-1

            (
                ffmpeg
                .input(f'{folder}/*.jpg', pattern_type='glob', framerate=30)
                .output(f'{folder}/flight_vid.mp4')
                .run()
            )
            print(f"Made video for {folder}")

    except Exception as e:
        print(f"Error making video for {folder}: {e}")