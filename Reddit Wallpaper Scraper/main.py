import ctypes
SPI_SETDESKWALLPAPER = 20 
path = "C:\\Users\\cnilo\\Documents\\Python Portfolio\\Reddit Wallpaper Scraper\\test2.png"
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)
print(path)

"""https://dev.to/matin/change-your-windows-background-by-running-a-python-script-281p"""