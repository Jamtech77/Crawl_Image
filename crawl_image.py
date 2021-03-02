import requests
import time, random
import os

user_input = input("Insert to download picture: ")

headers = {
    "User-Agent": "Search 'what is my user agent' in browser"
}

response = requests.get(f"https://unsplash.com/napi/search?query={user_input}&per_page=20&xp=feedback-loop-v2%3Acontrol", headers = headers)

for index in range(10):
    url = response.json()["photos"]["results"][index]["links"]["download"]

    if not os.path.exists("images"):
        os.mkdir("images")

    time.sleep(random.uniform(1,3))
    img = requests.get(url, headers = headers)

    with open("images\\" + user_input + str(index + 1) + ".jpg", "wb") as file:
        file.write(img.content)
