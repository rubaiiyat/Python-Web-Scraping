import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url = requests.get(
    "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
)

soup = BeautifulSoup(url.text, "lxml")


Title = []
titles = soup.find_all("a", class_="title")
for title in titles:
    Title.append(title.text)


Price = []
prices = soup.find_all("h4", class_="price float-end card-title pull-right")
for p in prices:
    Price.append(p.text)


Description = []
dess = soup.find_all("p", class_="description card-text")
for des in dess:
    Description.append(des.text)


review = []
reviews = soup.find_all("p", class_="review-count float-end")
for r in reviews:
    review.append(r.text)


dataFr = pd.DataFrame(
    {
        "Product Name": Title,
        "Price": Price,
        "Description": Description,
        "Reviews": review,
    }
)


dataFr.to_excel("Product.xlsx")
