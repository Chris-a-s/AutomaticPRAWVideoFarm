# PRAW Video Farm

## IMPORTANT NOTES 
- PRAW has become a paid API, meaning this program is no longer free.
- The code worked back in January 2023, however, tests of it in May ran multiple errors.
- With the execution of this program now costing money, interest in this program has diminished.
- I had written a program to upload the videos on YouTube, and all demo videos are uploadable to YouTube. Still, I have left it out because I need to double-check for sensitive information. Once it is cleared, I will update the repository.
- There are a lot of imports that aren't necessary in the version I uploaded, feel free to clear it out for your own code.

## Why it was written
This program was written to download videos with youtube-dl on Reddit, compile it with moviePy, and upload these results onto YouTube. The resulting video will be a compilation, and it even has an intro and outro that gets added too. I chose to do TikTok Cringe Compilations since the subreddit around it was very popular at the time and I could do much more frequent uploads. This can be any compilation video as long as it is on an existing, and hopefully thriving, subreddit.

## How to use
- Register for all APIs that would need to be used and plug in your keys where it states to
- Pick your subreddit where I have added that variable
- Select your count for how many subreddit posts you want the algorithm to go through. **NOTE** This is NOT how many videos you want, this is how many posts you would like the program to scroll through. Going through 30 posts will lead to any number from 0 to 30 videos, and when I ran demos on my computer, I typically got somewhere in the low to mid-20s.
- You will need four files on your computer, ideally within a larger channel folder. These will be your Intro, Outro, Scraped, and Final folders. It is important that I quickly explain each folder. Intro and Outro should have one video in each folder prior to execution. The scraped folder is where all of the videos will be downloaded, creating the compilation. Finally, the Final folder will be where the final product goes, taking videos from Intro, then Scraped, and Outro. This will then be ready for uploading to YouTube.
- I have written "CONFIGURE: XYZ" in the code so that it would be easier for users to make their own video maker.


### [Demo Channel](https://www.youtube.com/@TikToktor)
