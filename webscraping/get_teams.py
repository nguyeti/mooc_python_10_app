# teams
# division, team, short_prefix, long_prefix, url
import requests
import pandas
from bs4 import BeautifulSoup

url = "http://www.espn.com/nba/teams"
r = requests.get(url)
c = r.content
soup = BeautifulSoup(c,"html.parser")

all = soup.find_all("div",{"class":"mod-container mod-open-list mod-teams-list-medium mod-no-footer"})
print(all[2].prettify())
l=[]

for division in all:
    division_contents = division.find_all("ul",{"class":"medium-logos"})
    for item in division_contents:
        teams = item.find_all("li")
        for team in teams:
            d={}
            d["division"] = division.h4.text
            d["team"] = team.h5.a.text
            d["short_prefix"] = team.h5.a["href"].split("/")[-2]
            d["long_prefix"] = team.h5.a["href"].split("/")[-1]
            d["url"] = team.h5.a["href"]
            l.append(d)


df=pandas.DataFrame(l)
df
df.to_csv("nba_teams.csv", index=False)
