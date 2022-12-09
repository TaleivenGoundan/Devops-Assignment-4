import requests
import json

def Cat():
    f = r"https://api.thecatapi.com/v1/images/search?limit=1"
    page = requests.get(f)
    data = json.loads(page.text)
    return(data[0]["url"])

Cat()

