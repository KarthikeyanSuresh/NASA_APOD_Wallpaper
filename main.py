import os
import time
from read_image import readImage
from resize_image import resizeImage
from set_wallpaper import setWallpaper

today = time.strftime("%Y-%m-%d")
api_key = os.environ["NASA_API_KEY"]
path = os.path.dirname(os.path.abspath("resized_image.png"))
path = path + "\\resized_image.png"

readImage(api_key, today)
resizeImage("wallpaper.png", "resized_image.png", 2560, 1440)
setWallpaper(path)