import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/phones/touch")


soup = BeautifulSoup(url.text, "lxml")


title = soup.find_all("a", class_="title")
title_list = []
for t in title:
    title_list.append(t.text)

price = soup.find_all("h4", class_="price float-end card-title pull-right")
price_list = []
for p in price:
    price_list.append(p.text)


description = soup.find_all("p", class_="description card-text")
des_list = []
for d in description:
    des_list.append(d.text)

review = soup.find_all("p", class_="review-count float-end")
rev_list = []
for r in review:
    rev_list.append(r.text)


productList = pd.DataFrame(
    {
        "Name": title_list,
        "Price": price_list,
        "Description": des_list,
        "Review": rev_list,
    }
)

productList.to_csv("ProductList.csv")
