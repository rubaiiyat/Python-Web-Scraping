import requests

from bs4 import BeautifulSoup

url = requests.get("https://books.toscrape.com/")


soup = BeautifulSoup(url.text, "html.parser")

print(soup.prettify())
