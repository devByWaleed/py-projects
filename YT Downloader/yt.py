# Importing Library
# import pytube
from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=WXqOc-oor-E"

file_path = "D:/Waleed/Work/New folder/py projects/YT Downloader"

try:
    yt = YouTube(video_url)
except:
    print(f"Connection Error!!")


mp4_streams = yt.streams.filter(file_extension='mp4').all()

download_video = mp4_streams[-1]

try:
    download_video.download(output_path=file_path)
    print(f"Downloaded The Video Successfully..")
except:
    print("Some Errors!")

