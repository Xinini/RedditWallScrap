import ctypes
import os
import config
import praw
import requests
from PIL import Image

#Identification from config.py
CLIENT_ID = config.clientID
CLIENT_SECRET = config.clientSecret
USERNAME = config.username
PASSWORD = config.password
USER_AGENT = "RedditWallScraperz"


#Making a reddit instance
reddit = praw.Reddit(client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     username = USERNAME,
                     password = PASSWORD,
                     user_agent = USER_AGENT
                     )

wallpapper_sub = reddit.subreddit(display_name="wallpaper").top(time_filter = "day", limit=1)

for post in wallpapper_sub:
    if not post.stickied:
        print(post.title + " " + post.url)
    data = requests.get(post.url).content
    f = open("img.jpg", "wb")
    f.write(data)
    f.close()
    img = Image.open("img.jpg")
    img.show()  


SPI_SETDESKWALLPAPER = 20 

fileName = "img.jpg"
#path = "test2.png"
path = "C:\\Users\\cnilo\\Documents\\Python Portfolio\\" + fileName
print(path)
#path = os.getcwd().split(">")[0]
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
#print(path)

"""https://dev.to/matin/change-your-windows-background-by-running-a-python-script-281p"""