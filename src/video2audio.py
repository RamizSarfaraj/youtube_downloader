import moviepy.editor as mp
from moviepy.editor import *
import os
import sys


input_path = input(str("Enter the path of the file :  "))
target_path = input(str("\nEnter the target path: "))


def video2audio(input_path, target_path):
    file = input(str("\nFile name (with extension) : "))
    file_path = os.path.join(input_path, file)
    clip = mp.AudioFileClip(file_path)

    newfile =  input(str("\n\nEnter the converted file name \n(without the extension, output will be .mp3) :  "))
    output_file = os.path.join(target_path, newfile + ".mp3")
    clip.write_audiofile(output_file)
    print("\n\n\ncomplete")

    question = input(str("\n\n\nDo you want to DELETE the video file : [y/n]"))
    if question == 'y' or 'Y':
        os.remove(file_path)
    else: 
        print("Quitting.")

video2audio(input_path, target_path)