from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_videoclips
from config import SUBREDDIT
import os

def combine_videos(videos, sounds):
          
    # video_files = [VideoFileClip(file, audio=True).resize((80, 60)) for file in videos]
    video_files = [VideoFileClip(file, audio=True).resize((1280, 720)) for file in videos]
    sound_files = [AudioFileClip(file) for file in sounds]
    for i in range(len(video_files)):
        if video_files[i].audio != None:
            new_sound_file = CompositeAudioClip([video_files[i].audio, sound_files[i]])
        else:
            new_sound_file = sound_files[i]

        video_files[i].audio = new_sound_file

    output_path = f"{os.path.join(os.getcwd(), SUBREDDIT)}.mp4"
    final_clip = concatenate_videoclips(video_files)
    final_clip.write_videofile(filename=output_path, codec='libx264', audio_codec='aac')


if __name__ == "__main__":
    pass
