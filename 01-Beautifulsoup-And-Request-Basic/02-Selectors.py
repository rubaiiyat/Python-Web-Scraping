import requests
from bs4 import BeautifulSoup

url = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(url.text, "html.parser")

title = soup.find("title").text


all_quote = soup.find_all("div", class_="quote")


for quote in all_quote:
    q = quote.find("span", class_="text").text


# Find Parent Sibling

title = soup.find("div", class_="col-md-4 tags-box")
""" print(title.parent())
print(title.find_next_sibling())
print(title.find_previous_sibling()) """

# children

children = title.children
childList = list(children)

unique_list = set(child.text for child in childList)
""" print(len(unique_list))

for child in unique_list:
    print(child) """


top_tag_a = title.a
top_tag_href = top_tag_a["href"]
print(top_tag_href)
