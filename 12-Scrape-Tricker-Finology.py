import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://ticker.finology.in/")
# print(url)

soup = BeautifulSoup(url.text, "lxml")
# print(soup)

header = soup.find("thead")
title = header.find_all("th")
titles = []
for t in title:
    titles.append(t.text.strip())

# print(titles)

dt = pd.DataFrame(columns=titles)
# print(dt)


tableBody = soup.find("tbody")
# print(tableBody)

rows = tableBody.find_all("tr")
# print(row)

for r in rows[1:]:
    data = r.find_all("td")
    # print(data)

    row = [tr.text.strip() for tr in data]
    l = len(dt)
    dt.loc[l] = row

print(dt)
