import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://www.iplt20.com/auction")

soup = BeautifulSoup(url.text, "lxml")


header = soup.find("div", class_="auction-grid-view mt-3")

teamName = header.find_all("div", class_="agv-team-name")
teamList = []
for n in teamName:
    teamList.append(n.text)

fund = header.find_all("div", class_="avg-fund-remaining")
fundList = []
for f in fund:
    amount = f.find("span", class_="fr-fund")
    fundList.append(amount.text)


Overseays = header.find_all("li", class_="m-0")
overseays = []
for o in Overseays:
    over = o.find("span", class_="fr-fund")
    overseays.append(over.text)

overseaysList = []
for i in range(len(overseays)):
    if i % 2 == 0:
        overseaysList.append(overseays[i])


TotalPlayers = []
for i in range(len(overseays)):
    if i % 2 != 0:
        TotalPlayers.append(overseays[i])


df = pd.DataFrame(
    {
        "Team Name": teamList,
        "Funds Remaining": fundList,
        "Overseas Players": overseaysList,
        "Total Players": TotalPlayers,
    }
)

df.to_csv("IPL_Auction.csv")
