import requests
from bs4 import BeautifulSoup
import pandas as pd

quotes = {"content": [], "author": [], "category": []}


page = 1
while True:
    print("---", page, "--->", end=" ")
    url = requests.get(f"https://quotes.toscrape.com/page/{page}/")
    soup = BeautifulSoup(url.text, "html.parser")
    mainDiv = soup.find_all("div", class_="quote")
    print(len(mainDiv))

    next = soup.find("li", class_="next")
    if next is None:
        break
    else:
        page += 1

    for div in mainDiv:
        content = div.find("span", class_="text").text
        quotes["content"].append(content)

        author = div.find("small", class_="author").text
        quotes["author"].append(author)

        tags = div.find_all("a", class_="tags")
        tag_list = [tag.text for tag in tags]

        quotes["category"].append(",".join(tag_list))


df = pd.DataFrame(quotes)

df.to_csv("Books.csv")

print("Perfectly Done")
