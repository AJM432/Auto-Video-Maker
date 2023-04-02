from moviepy.editor import VideoFileClip, concatenate_videoclips

def combine_videos(videos):
    clips = [VideoFileClip(vid, audio=False).resize((480, 360)) for vid in videos]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("my_concatenation.mp4")

if __name__ == "__main__":
    pass
