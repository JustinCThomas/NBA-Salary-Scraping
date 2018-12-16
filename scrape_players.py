import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.basketball-reference.com/contracts/players.html"

req = requests.get(url)
content = req.content
soup = BeautifulSoup(content, "html.parser")
player_table = soup.find(id="player-contracts")
print(player_table)
