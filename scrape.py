import praw
from redvid import Downloader
from dotenv import dotenv_values
import os
import gtts
from config import SUBREDDIT, SCRAPE_LIMIT, MAX_VIDEO_DURATION

def authenticate():
    config = dotenv_values(".env")
    CLIENT_ID = config['CLIENT_ID']
    SECRET_TOKEN = config['SECRET_TOKEN']
    user = config['user']
    password = config['password']

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=SECRET_TOKEN,
        user_agent=f"AutoVideo 1.0 by /u/{user}",
        username=user,
        password=password,
    )
    return reddit

def scrape_videos(limit=SCRAPE_LIMIT, duration=60, subreddit=SUBREDDIT):
    reddit = authenticate()
    vids = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        try:
            if submission.media["reddit_video"]["duration"] < duration:
                vids.append(submission)
        except:
            pass
    return vids

def download_videos():
    vids = scrape_videos(duration=MAX_VIDEO_DURATION)
    down = Downloader(max_q=True)
    down.auto_max = True
    down.max_s = 3 * (1 << 20) # wont exceed 3mb
    for vid in vids:
        download_path = os.path.join(os.getcwd(), "videos", vid.id)
        down.path = download_path
        down.url = vid.url
        down.download()

        tts = gtts.gTTS(vid.title)
        tts.save(os.path.join(download_path, f"{vid.id}.mp3"))
    return vids # keep info of clip origin

if __name__ == '__main__':
    download_videos()


