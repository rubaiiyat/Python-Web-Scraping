import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.amazon.com/",
}

for i in range(2, 3):
    url = requests.get(
        f"https://www.amazon.com/s?k=acoustic+guitar&page={i}&qid=1725470944&ref=sr_pg_{i}",
        headers=headers,
    )

    soup = BeautifulSoup(url.text, "lxml")

    title = soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")
    titleList = []
    for t in title:
        titleList.append(t.text)

    df = pd.DataFrame({"Guitar Name": titleList})
    print(df)
