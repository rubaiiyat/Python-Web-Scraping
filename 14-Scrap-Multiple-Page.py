import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
for i in range(2, 11):
    url = requests.get(
        f"https://www.flipkart.com/search?q=acoustic%20guitar&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    )

    soup = BeautifulSoup(url.text, "lxml")

    """ if url.status_code == 200:
        print(
            f"https://www.flipkart.com/search?q=acoustic%20guitar&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
        ) """

    if url.status_code == 200:
        np = soup.find("a", class_="_9QVEpD").get("href")
        nextPage = "https://www.flipkart.com" + np
        print(nextPage)
    time.sleep(10)
