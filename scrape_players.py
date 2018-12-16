import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = "https://www.basketball-reference.com"

req = requests.get(base_url + "/contracts/players.html")
content = req.content
soup = BeautifulSoup(content, "html.parser")
player_table = soup.find(id="player-contracts")
player_rows = player_table.find("tbody").find_all("tr", {"data-row": ""})


for i in player_rows:
    if i.find("a") == None:
        continue

    player_link = i.find("a")
    print(player_link)
