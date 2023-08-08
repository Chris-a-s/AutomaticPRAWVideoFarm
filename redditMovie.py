
#Import things for project
import praw
import subprocess
import time
from moviepy.editor import *
import os
import moviepy.video.fx.all as vfx
from moviepy.video.io.VideoFileClip import VideoFileClip
import datetime
import time
from googleapiclient.http import MediaFileUpload
import pandas as pd
from google_apis import create_service





# CONFIGURE: PRAW information
reddit = praw.Reddit(
                    client_id='YOUR CLIENT ID',
                    client_secret='YOUR CLIENT SECRET',
                    username='YOUR USERNAME',
                    password='YOUR PASSWORD',
                    user_agent='YOUR USER AGENT')

# CONFIGURE: Subreddit of choice
subreddit = reddit.subreddit('Pick Subreddit')

# CONFIGURE: Scraped Folder
folder = "\\PATH\\TO\\Scraped"

# CONFIGURE: subreddit search and limit
posts = subreddit.search("flair:CHOOSE FLAIR", sort='Choose Sort', limit=20) # Set the limit to whatever you want

# iterate through the posts
for post in posts:
    # check if the post is a video
    if post.is_video:
        # get the url of the video
        url = post.url
        # get the title of the video
        title = post.title[:30].rstrip() + ".mp4"
        # download the video using youtube-dl
        subprocess.call(['youtube-dl', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]', '-o', f'{folder}/{title}', url])
    else:
        print(f'{post.title} is not a video post, skipping...')

print("Done! Now go make sure the folder is not corrupt")
    
#Rest Program for a certain amount of time while you siphon through files in folder to make sure everything works
time.sleep(30)

# PART TWO: EDIT THE VIDEOS FROM THE FILE USING MOVIEPY

#Set resolution
width = 1920
height = 1080

# CONFIGURE: INTRO AND OUTRO FOLDER
intro_folder = "Path\\To\\Intro"

outro_folder = "Path\\To\\Outro"


intro = VideoFileClip(os.path.join(intro_folder, "intro.mp4"))
outro = VideoFileClip(os.path.join(outro_folder, "outro.mp4"))

# get all of the videos in the scraped folder

video_files = [file for file in os.listdir(folder) if file.endswith(".mp4")]


# Create clips for each of the re-encoded videos
video_clips = [VideoFileClip(os.path.join(folder, file)) for file in os.listdir(folder) if file.endswith(".mp4")]

resized_videos = [vfx.resize(clip, height=height) for clip in video_clips]

# Concatenate the intro, videos, and outro
compilation = concatenate_videoclips(([intro] + resized_videos + [outro]), method='compose')

# CONFIGURE: FINAL FOLDER AND NAME OF VIDEO FILE
compilation.write_videofile("PATH\\TO\\Final\\videofile.mp4")

