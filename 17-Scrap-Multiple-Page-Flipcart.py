import requests
import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=acoustic+guitar&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_9_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_9_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=acoustic+guitar&requestId=979dca32-ba12-41f5-8d46-7514f22ada35&as-backfill=on"
scraper = cloudscraper.create_scraper()
res = scraper.get(url)
print(res)


soup = BeautifulSoup(res.text, "lxml")

nameList = []
priceList = []
TotalRev = []
reviewList = []

name = soup.find_all("a", class_="wjcEIp")

for i in name:
    nameList.append(i.text)

price = soup.find_all("div", class_="Nx9bqj")
for p in price:
    priceList.append(p.text)


review = soup.find_all("div", class_="XQDdHH")
for r in review:
    reviewList.append(r.text)


totalRev = soup.find_all("span", class_="Wphh3N")
for t in totalRev:
    TotalRev.append(t.text)

print(TotalRev)

""" df = pd.DataFrame({"priceList": priceList})
print(df) """
