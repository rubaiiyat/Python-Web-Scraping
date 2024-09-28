import requests
from bs4 import BeautifulSoup
import pandas as pd

book_dict = {
    "Name": [],
    "Price": [],
    "Category": [],
    "UPC": [],
    "Star": [],
    "Stock": [],
    "Img": [],
}


page_no = 1

while True:
    print(f"Page---{page_no}--->", end=" ")
    next_url = f"https://books.toscrape.com/catalogue/page-{page_no}.html"

    response = requests.get(next_url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    print(len(books))
    next = soup.find("li", class_="next")
    if next is None:
        break
    else:
        page_no += 1

    for book in books:
        book_url = "https://books.toscrape.com/catalogue/" + book.find("a")["href"]
        url = requests.get(book_url)

        url.encoding = "utf-8"
        soup = BeautifulSoup(url.text, "html.parser")

        mainDiv = soup.find("div", class_="col-sm-6 product_main")

        name = mainDiv.find("h1").text
        book_dict["Name"].append(name)

        price = mainDiv.find("p", class_="price_color").text
        book_dict["Price"].append(price)

        rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = mainDiv.find("p", class_="star-rating")
        start_rating = rating["class"]
        star_string = start_rating[1]
        star = rating_dict[star_string]
        book_dict["Star"].append(star)

        mainCat = soup.find("ul", class_="breadcrumb")
        ulList = soup.find_all("li")
        category = ulList[2].a.text
        book_dict["Category"].append(category)

        upc = soup.find("th", string="UPC").text
        book_dict["UPC"].append(upc)

        stock = soup.find("th", string="Availability")
        available = stock.find_next_sibling().text
        availability = "".join([char for char in available if char.isdigit()])
        book_dict["Stock"].append(availability)

        imgMain = soup.find("div", class_="item active").img["src"]
        img_url = "https://books.toscrape.com/" + imgMain[6:]
        book_dict["Img"].append(img_url)


df = pd.DataFrame(book_dict)

df.to_csv("Books.csv")

print("Perfectly Done")
