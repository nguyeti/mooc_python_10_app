import pandas
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


teams = pandas.read_csv("nba_teams.csv", usecols=['short_prefix'])
for team_prefix in teams["short_prefix"]:
    l=[]
    for year in range(2003,2017,1):
        url ="http://www.espn.com/nba/team/schedule/_/name/{0}/year/{1}"
        print(url.format(team_prefix,str(year)))
        r = requests.get(url.format(team_prefix,str(year)))
        c = r.content
        soup = BeautifulSoup(c,"html.parser")
        all = soup.find("div",{"class":"mod-content"})

        all_rows = all.find_all("tr",class_=re.compile(r"(even|odd)row"))
        all_rows


        for row in all_rows:
            row_details = row.find_all("td")
            d={}
            for detail,i in zip(row_details,range(0,len(row_details))):        
                #print(i,detail.text)
                if i == 0:
                    d["date"] = datetime.strptime(detail.text + " " + str(year),"%a, %b %d %Y")
                elif i == 1:
                    _home = True if "vs" in detail.text else False
                    _team = BeautifulSoup(c,"html.parser").find("h2",{"class":"logo"}).text.split(" ")[0]
                    _other_team = detail.text.replace("@","").replace("vs","")
                    d["home_team"] =  _team if _home else _other_team
                    d["visit_team"] = _team if not _home else _other_team
                    #d["location"] = "home" if "vs" in detail.text else "away"   
                elif i == 2:
                    #d["result"] = detail.text[0]
                    #d["result_score"] = detail.text[1:]
                    _won = True if "W" in detail.text[0] else False
                    _score = detail.text[1:].split("-") if detail.text not in ["Postponed","Canceled"] else "--"
                    #print(_score)

                    if _home:
                        if _won:
                            d["home_team_score"]=_score[0]
                            d["visit_team_score"]=_score[1]
                        else:
                            d["home_team_score"]=_score[1]
                            d["visit_team_score"]=_score[0]
                    else:
                        if _won:
                            d["home_team_score"]=_score[1]
                            d["visit_team_score"]=_score[0]
                        else:
                            d["home_team_score"]=_score[0]
                            d["visit_team_score"]=_score[1]
                #elif i == 3:
                 #   d["current w/l"] = str(detail.text)
                #elif i == 4:
                 #   d["hi_points"] = detail.text
                #elif i == 5:
                 #   d["hi_rebounds"] = detail.text
                #elif i == 6:
                 #   d["hi_assists"] = detail.text
            l.append(d)
        df = pandas.DataFrame(l)
        df.to_csv("{0}_{1}_games.csv".format(str(year),team_prefix), index=False, date_format='%Y-%m-%d')
        print("saving to " + "{0}_{1}_games.csv".format(str(year),team_prefix))
