import requests
from bs4 import BeautifulSoup


quotes = {"content": [], "author": [], "category": []}

url = requests.get("https://quotes.toscrape.com/page/1/")

soup = BeautifulSoup(url.text, "html.parser")


mainDiv = soup.find("div", class_="quote")

content = mainDiv.find("span", class_="text").text
quotes["content"].append(content)

author = mainDiv.find("small", class_="author").text
quotes["author"].append(author)

tags = mainDiv.find_all("div", class_="tags")
for t in tags:
    all_tag = t.find_all("a", class_="tag")
    for tag in all_tag:
        quotes["category"].append(tag.text)


print(quotes)
