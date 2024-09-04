import requests
from bs4 import BeautifulSoup

for i in range(1, 10):
    url = requests.get(
        f"https://www.daraz.com.bd/catalog/?page={i}&q=acoustic%20guitar&spm=a2a0e.tm80335401.search.d_go"
    )

    soup = BeautifulSoup(url.text, "lxml")

    if url.status_code == 200:
        print(
            f"https://www.daraz.com.bd/catalog/?page={i}&q=acoustic%20guitar&spm=a2a0e.tm80335401.search.d_go"
        )
