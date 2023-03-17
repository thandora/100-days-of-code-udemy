""" Parses https://news.ycombinator.com/ to get the most upvoted article
and print it out. This is an exercise on using bs4.
"""

from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.ycombinator.com/")
html = r.text
soup = BeautifulSoup(html, features="html.parser")

articles_raw = soup.select(".athing")
articles = []

for article in articles_raw:
    article_id = article.get("id")
    score_id = "score_" + article_id
    article_title = article.select_one(".titleline a").get_text()
    article_link = article.select_one(".titleline a").get("href")
    try:
        score = soup.find(name="span", id=score_id).get_text()
    except AttributeError:
        article_score = 0
    else:
        article_score = int(score.split()[0])
    articles.append(
        {
            "id": article_id,
            "title": article_title,
            "score": article_score,
            "link": article_link,
        }
    )

# Create list of lists [ [<score1>, <article_dict1>], ...]
scores = [[article.get("score"), article] for article in articles]

print(max(scores))
