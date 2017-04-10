import pandas, requests, re
from bs4 import BeautifulSoup
from datetime import datetime

def get_year():
    return str(datetime.now().year)

def get_soup(team_name_short, team_name_long):
    base_url = "http://www.espn.com/nba/team/roster/_/name/{0}/{1}"
    r = requests.get(base_url.format(team_name_short,team_name_long))
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    return soup

def get_rosters(short_team_name_col,long_team_name_col):
    print("***** START *****")
    for short_team_name,long_team_name in zip(short_team_name_col,long_team_name_col):
        soup = get_soup(short_team_name,long_team_name)
        table = soup.find_all("div",{"class":"mod-container mod-table mod-no-header-footer"})

        all_rows = []
        for content in table:
            rows = content.find_all("tr", class_=re.compile(r"(even|odd)row"))
            for row, info_nb in zip(rows,range(1,len(rows)+1)):
                player_infos ={}
                row_cols = row.find_all("td")
                for col, col_nb in zip(row_cols,range(0,len(row_cols))):
                    if col_nb == 0:
                        player_infos["player_number"] = col.text
                    elif col_nb == 1:
                        player_infos["player_name"] = col.text
                    elif col_nb == 2:
                        player_infos["player_pos"] = col.text
                    elif col_nb == 3:
                        player_infos["player_age"] = col.text
                    elif col_nb == 4:
                        player_infos["player_height"] = col.text
                    elif col_nb == 5:
                        player_infos["player_weight"] = col.text
                    elif col_nb == 6:
                        player_infos["player_college"] = col.text
                    elif col_nb == 7:
                        player_infos["player_salary"] = col.text
                all_rows.append(player_infos)

        df = pandas.DataFrame(all_rows)
        df.to_csv("{0}_{1}_roster.csv".format(get_year(), short_team_name), index=False)
        print("saving {0} roster to {1}_{2}_roster.csv".format(long_team_name,get_year(), short_team_name))
    print("***** END *****")

df = pandas.read_csv("nba_teams.csv", usecols=['short_prefix','long_prefix'])
get_rosters(df["short_prefix"], df["long_prefix"])