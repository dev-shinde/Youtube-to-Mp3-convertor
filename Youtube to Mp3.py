import pytube
from pytube import YouTube

url = input("\nEnter your video URL\n\n")

video_url = url

yt = YouTube(video_url)

audio_stream = yt.streams.filter(only_audio=True).first()

audio_stream.download()

name = input("\n\nEnter name you want to give to the file\n\n")

audio = name+".mp3"

import os
os.rename(audio_stream.default_filename, audio)
