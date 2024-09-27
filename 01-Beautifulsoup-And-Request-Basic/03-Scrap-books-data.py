import requests
from bs4 import BeautifulSoup

url = requests.get(
    "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
)


url.encoding = "utf-8"
soup = BeautifulSoup(url.text, "html.parser")

mainDiv = soup.find("div", class_="col-sm-6 product_main")

name = mainDiv.find("h1")
print(name.text)

price = mainDiv.find("p", class_="price_color").text
print(price)


rating_dict = {"One": 1, "Two": 2, "Three": 3, " Four": 4, " Five": 5}
rating = mainDiv.find("p", class_="star-rating")
start_rating = rating["class"]
star_string = start_rating[1]
star = rating_dict[star_string]
print(star)


mainCat = soup.find("ul", class_="breadcrumb")
ulList = soup.find_all("li")
print(ulList[2].a.text)


upc = soup.find("th", string="UPC").text
print(upc)

stock = soup.find("th", string="Availability")
available = stock.find_next_sibling().text
availability = "".join([char for char in available if char.isdigit()])
print(availability)
