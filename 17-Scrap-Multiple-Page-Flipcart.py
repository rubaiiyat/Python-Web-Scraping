import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

nameList = []
priceList = []
reviewList = []
TotalRev = []

for i in range(0, 16):
    scraper = cloudscraper.create_scraper()
    url = (
        "https://www.flipkart.com/search?q=acoustic+guitar&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_9_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_9_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=acoustic+guitar&requestId=979dca32-ba12-41f5-8d46-7514f22ada35&as-backfill=on&sort=relevance&page="
        + str(i)
    )
    res = scraper.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    box = soup.find("div", class_="DOjaWF YJG4Cf")  # Container for the products

    if box:
        # Names
        names = box.find_all("a", class_="wjcEIp")
        page_name_list = [name.text for name in names]

        # Prices
        prices = box.find_all("div", class_="Nx9bqj")
        page_price_list = [price.text for price in prices]

        # Reviews
        reviews = box.find_all("div", class_="XQDdHH")
        page_review_list = [
            reviews[i].text if i < len(reviews) else "0"
            for i in range(len(page_name_list))
        ]

        # Total Reviews
        total_reviews = box.find_all("span", class_="Wphh3N")
        page_total_rev_list = [
            total_reviews[i].text if i < len(total_reviews) else "0"
            for i in range(len(page_name_list))
        ]

        # Append current page data to the main lists
        nameList.extend(page_name_list)
        priceList.extend(page_price_list)
        reviewList.extend(page_review_list)
        TotalRev.extend(page_total_rev_list)

        # Print status after each page
        print(
            f"Page {i} - Names: {len(nameList)}, Prices: {len(priceList)}, Reviews: {len(reviewList)}, Total Reviews: {len(TotalRev)}"
        )

# Create a DataFrame
df = pd.DataFrame(
    {
        "Name": nameList,
        "Price": priceList,
        "Review": reviewList,
        "Total Review": TotalRev,
    }
)

# Save the DataFrame to a CSV file
df.to_csv("18-Flipkart_products.csv", index=False)
