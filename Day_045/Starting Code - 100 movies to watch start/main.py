import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

content = requests.get(URL)

soup = BeautifulSoup(content.text, "html.parser")
list_of_movies = soup.find_all(name="h3", class_="title")

with open("./top-100-movie-list.txt", "w") as writer:
    for t in list_of_movies[::-1]:
        writer.write(t.get_text() + "\n")