import requests
from bs4 import BeautifulSoup

url = "https://www.wscubetech.com/"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
print(soup)
