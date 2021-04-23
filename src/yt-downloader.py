from moviepy.editor import *
import moviepy.editor as mp
from pytube import YouTube
import os
import re
import sys


def audio_downloader():
    """
    This function downloads the audio format of the youtube video.
    """
    yt_link = input(str("Enter the link : "))
    audio = YouTube(yt_link)

    title = audio.title

    t = audio.streams.filter(only_audio=True, adaptive=True, file_extension='mp4').all() # extracting the audio information

    path = input(str("\n\nEnter the target directory : "))

    try:
        s = 1
        for v in t:
            print(str(s)+". "+str(v))
            print("\n")
            s += 1

        n = int(input("\n\nEnter the number of the video: "))
        aud = t[n-1]

        print("\nDownloading : " + title)
        aud.download(output_path=path) # downloads as mp4 without the video just the audio portion, technically a video.
        print("\n\nConverting to mp3")

        for file in [n for n in os.listdir(path) if re.search('mp4',n)]:
            full_path = os.path.join(path, file)
            output_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
            clip = mp.AudioFileClip(full_path) #.subclip(10,) # disable if do not want any clipping
            clip.write_audiofile(output_path)

        ans = input(str("\n\nDo you want to DELETE the mp4 file? [y/n] : " ))
        if ans == 'y' or 'Y':
            if os.path.exists(full_path):
                os.remove(full_path)
                print("\n\n\t\t\tDELETED\n\n")
            else: print("\n\nFile does not exist.")
        else: print("Aborting Operation")

    except Exception as ec:
        print("\n\nSomethings wrong.\n\n")
        print(ec)


def video_downloader():


    yt_link = input(str("Enther the link : "))
    video = YouTube(yt_link)

    title = video.title

    # v = video.streams.filter().all()# extracting the video information
    v = video.streams.get_highest_resolution()
    # adaptive filter lists the best quality first
    path = input(str("\n\nEnter the target directory : "))

    try:
        # s = 1
        # for i in v:
            # print(str(s)+". "+str(i))
            # print("\n")
            # s += 1

        # n = int(input("Enter the number of the video: "))
        # vid = v[n-1]
        vid = v

        print("\nDownloading the video file :: " + title)
        vid.download(output_path=path)
        print("\n\nCompleted.")

    except:
        print("\n\nSomethings wrong.")

if __name__ == '__main__':
    while True:

        print("\n\na. Activate audio downloader.")
        print("b. Activate video downloader.")
        print("q. Quit.\n\n")

        ans = input(str("Enter your choice : "))
        print("\n\n")

        if ans == "a":
            print("----------Audio Downloader Activated----------")
            print("\n\n")
            audio_downloader()
            break

        elif ans == "b":
            print("----------Video Downloader Activated----------")
            print("\n\n")
            print("Video with pytube will not be the highest of qualities out there.")
            video_downloader()
            break

        elif ans == "q":
            print("Aborting Operation")
            break

        else:
            print("Wrong Input. Try Again.")
