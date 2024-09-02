import requests
from bs4 import BeautifulSoup


url = requests.get("https://ticker.finology.in/")

soup = BeautifulSoup(url.text, "lxml")

tables = soup.find("table", class_="table table-sm table-hover screenertable")

title = tables.find_all("th")
title_list = []

for t in title:
    title_list.append(t.text)
