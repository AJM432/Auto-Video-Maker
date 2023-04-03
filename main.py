from scrape import download_videos
from make_video import combine_videos
from scrape import download_videos
import os, shutil

download_videos()

video_folder = os.path.join(os.getcwd(), "videos")
video_files = []
sound_files = []

for root, dirs, files in os.walk(video_folder, topdown=False):
   for name in files:
       if name.endswith(".mp4"):
           video_files.append(os.path.join(root, name))
       elif name.endswith(".mp3"):
           sound_files.append(os.path.join(root, name))

combine_videos(video_files, sound_files)
shutil.rmtree(video_folder)
os.mkdir('videos')

