import requests
from bs4 import BeautifulSoup

url = requests.get("https://webscraper.io/test-sites/e-commerce/allinone")
soup = BeautifulSoup(url.text, "lxml")
print(soup.div)
