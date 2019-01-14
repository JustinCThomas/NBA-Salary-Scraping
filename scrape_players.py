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
    players_scraped = 0
    data_row = 0
    # f = open("nba_players.csv", "w")
    for i in player_rows:
        if players_scraped >= amount:
            break
        if i.find("a") == None:
            data_row += 1
            continue

        player_link = i.find("a")['href']
        player_name = i.find("a").get_text()

        req = requests.get(base_url + player_link)
        content = req.content
        soup = BeautifulSoup(content, "html.parser")

        comment_container = soup.find(id="all_all_salaries")
        comments = comment_container.find(text=lambda text:isinstance(text, Comment))
        comment_soup = BeautifulSoup(comments, "html.parser")

        salary_table = comment_soup.find(id="all_salaries")
        salaries = salary_table.find("tbody").find_all("tr", {"data-row": ""})

        print("Scraping Player %s...\n" % player_name)
        for i in salaries:
            season = i.find("th").get_text()
            team = i.find_all("td")[0].find("a").get_text()
            if season[0] != "2":
                continue
            salary = i.find_all("td")[2]["csk"]

            print("Player: {} Team: {} Season: {} Salary: ${:,}".format(player_name, team, season, int(salary)))
            # season_stats = "{}, {}, {}, ${}\n".format(player_name, team, season, int(salary))
            # f.write(season_stats)

        # current_team = player_rows.find("tr")
        # .find("a").get_text()
        # current_team = player_table.find("tbody").find("tr").find_all("td", {"data-stat": "team_id"})[0]
        # current_team = player_table.find("tbody").find("tr")
        # print(current_team)
        # current_season = soup.title.get_text()[:7]
        # current_salary = player_rows.find_all("td", {"data-stat": "y1"})[0]["csk"]
        # print("Player: {} Team: {} Season: {} Salary: ${:,}".format(player_name, current_team, current_season, int(current_salary)))

        print()
        sleep(1)

        players_scraped += 1
        data_row += 1

if __name__ == "__main__":
    search_players()
