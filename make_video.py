from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def combine_videos(videos):
    video_path = os.path.join(os.getcwd(), "videos")
    clips = [VideoFileClip(vid).resize((480, 360)) for vid in videos]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(os.path.join(video_path, 'my_concatenation.mp4'))

if __name__ == "__main__":
    pass
