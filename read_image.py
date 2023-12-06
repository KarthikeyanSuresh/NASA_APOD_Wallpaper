import urllib.request
import requests

def readImage(api_key, date):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    response = requests.get(url)
    data = response.json()
    image = data['hdurl']
    urllib.request.urlretrieve(image, "wallpaper.png")

