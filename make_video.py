from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_videoclips
import os

def combine_videos(videos, sounds):
          
    # clips = [VideoFileClip(vid).resize((480, 360)) for vid in videos]
    video_files = [VideoFileClip(file, audio=True).resize((80, 60)) for file in videos]
    sound_files = [AudioFileClip(file) for file in sounds]
    for i in range(len(video_files)):
        if video_files[i].audio != None:
            new_sound_file = CompositeAudioClip([video_files[i].audio, sound_files[i]])
        else:
            new_sound_file = sound_files[i]

        video_files[i].audio = new_sound_file

    video_path = os.path.join(os.getcwd(), "videos")

    final_clip = concatenate_videoclips(video_files)
    final_clip.write_videofile(os.path.join(video_path, 'my_concatenation.mp4'))
    final_clip.write_videofile(filename=os.path.join(video_path, 'my_concatenation.mp4'),
                                codec='libx264',
                                audio_codec='aac')

if __name__ == "__main__":
    pass
