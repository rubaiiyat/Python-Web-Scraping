import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://ticker.finology.in/")

soup = BeautifulSoup(url.text, "lxml")


Headers = soup.find("table", class_="table table-sm table-hover screenertable")

title = Headers.find_all("th")
titles = []
for t in title:
    titles.append(t.text)

df = pd.DataFrame(columns=titles)

rows = Headers.find_all("tr")

for r in rows[1:]:
    data = r.find_all("td")
    row = [tr.text.strip() for tr in data]

    df.loc[len(df)] = data


print(df)
