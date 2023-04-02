from scrape import download_videos
from make_video import combine_videos
from scrape import download_videos
import os

download_videos()
video_folder = os.path.join(os.getcwd(), "videos")
mp4_files = []
for file in os.listdir(video_folder):
    if file.endswith(".mp4"):
        mp4_files.append(os.path.join(video_folder, file))

combine_videos(mp4_files)

