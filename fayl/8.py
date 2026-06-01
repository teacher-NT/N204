import os
os.system("cls")

from pytubefix import YouTube

link = input("Video linkini kiriting: ")
print("Ulanmoqda...")
yt = YouTube(link)
video = yt.streams.get_highest_resolution()
# video = yt.streams.get_by_resolution("360p")
# audio = yt.streams.get_audio_only()
print("Yuklanmoqda...")
video.download("videolar/")
# audio.download("videolar/")
print("Tayyor...")