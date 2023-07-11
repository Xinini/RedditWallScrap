import ctypes
import os
import config
import praw

#Identification from config.py
CLIENT_ID = config.clientID
CLIENT_SECRET = config.clientSecret
USERNAME = config.username
PASSWORD = config.password
USER_AGENT = "RedditWallScraperz"

reddit = praw.reddit(client_id = CLIENT_ID,
                     client_secret = CLIENT_SECRET,
                     username = USERNAME,
                     password = PASSWORD,
                     user_agent = USER_AGENT
                     )




SPI_SETDESKWALLPAPER = 20 

fileName = "test2.png"
#path = "test2.png"
#path = "C:\\Users\\cnilo\\Documents\\Python Portfolio\\Reddit Wallpaper Scraper\\test1.jpg"
#print(path)
#path = os.getcwd().split(">")[0]
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
#print(path)

"""https://dev.to/matin/change-your-windows-background-by-running-a-python-script-281p"""