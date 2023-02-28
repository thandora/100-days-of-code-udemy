from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, features="html.parser")

# Get the reversed order so it becomes top 1 to 100.
titles = soup.find_all(name="h3", class_="title")[::-1]
movies_list = []

with open("movies.txt", "w", encoding="utf-8") as f:
    for title in titles:
        f.write(title.get_text() + "\n")
