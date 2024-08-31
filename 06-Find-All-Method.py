import requests
from bs4 import BeautifulSoup
import re

url = requests.get(
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
)


soup = BeautifulSoup(url.text, "lxml")


title = soup.find_all(string=re.compile("Hewlett"))

print(len(title))
for t in title:
    print(t)
