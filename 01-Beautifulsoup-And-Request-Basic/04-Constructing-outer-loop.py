import requests
from bs4 import BeautifulSoup

url = requests.get("https://books.toscrape.com/")


soup = BeautifulSoup(url.text, "html.parser")

""" page_count = soup.find("li", class_="current").text
page = int(page_count.strip().split(" ")[-1])

for i in range(1, page + 1):
    print(f"Page---{i}--->", end=" ")
    next_url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    response = requests.get(next_url)
    soup = BeautifulSoup(response.text, "html.parser")
    li = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    print(len(li)) """


page_no = 45

while True:
    print(f"Page---{page_no}--->", end=" ")
    next_url = f"https://books.toscrape.com/catalogue/page-{page_no}.html"

    response = requests.get(next_url)
    soup = BeautifulSoup(response.text, "html.parser")
    li = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    print(len(li))
    next = soup.find("li", class_="next")
    if next is None:
        break
    else:
        page_no += 1
