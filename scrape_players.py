import requests
from bs4 import BeautifulSoup, Comment
from time import sleep

base_url = "https://www.basketball-reference.com"

req = requests.get(base_url + "/contracts/players.html")
content = req.content
soup = BeautifulSoup(content, "html.parser")
player_table = soup.find(id="player-contracts")
player_rows = player_table.find("tbody").find_all("tr", {"data-row": ""})


def search_players(amount=100):
    for i in player_rows:
        if amount <= 0:
            break
        if i.find("a") == None:
            continue

        player_link = i.find("a")['href']

        req = requests.get(base_url + player_link)
        content = req.content
        soup = BeautifulSoup(content, "html.parser")

        comment_container = soup.find(id="all_all_salaries")
        comments = comment_container.find(text=lambda text:isinstance(text, Comment))
        comment_soup = BeautifulSoup(comments, "html.parser")

        salary_table = comment_soup.find(id="all_salaries")
        salaries = salary_table.find("tbody").find_all("tr", {"data-row": ""})

        for i in salaries:
            season = i.find("th").get_text()
            salary = i.find_all("td")[2]["csk"]
            
            print("Season: {} Salary: ${:,}".format(season, int(salary)))

        # remove later
        break
        amount -= 1

if __name__ == "__main__":
    search_players()
