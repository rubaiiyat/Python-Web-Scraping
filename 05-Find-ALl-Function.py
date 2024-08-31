import requests
from bs4 import BeautifulSoup

url = requests.get(
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
)

soup = BeautifulSoup(url.text, "lxml")

fnd = soup.find_all("h4", class_="price")

for f in fnd:
    print(f.text)
