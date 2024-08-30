import requests
from bs4 import BeautifulSoup

url = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")

soup = BeautifulSoup(url.text, "lxml")

title = soup.find("a", {"class": "title"})
print(title.string)

des = soup.find("p", class_="description card-text")
print(des)
