import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.basketball-reference.com/contracts/players.html"

req = requests.get(url)
content = req.content
soup = BeautifulSoup(content, "html.parser")
player_table = soup.find(id="player-contracts")
player_rows = player_table.find("tbody").find_all("tr", {"data-row": ""})

player_link = player_rows[0].find("a")
print(player_rows[0])
print(player_link)

# while True:
