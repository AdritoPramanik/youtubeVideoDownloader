# modules needed
# pytube
# pip install pytube
from pytube import YouTube

link = input("Enter the link of the video that you wish to download")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
try:
    print("Downloading...")
    ys.download('F:/')
    print("Download Completed")

except:
    print("video not found")
