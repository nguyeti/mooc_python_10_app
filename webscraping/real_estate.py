import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
content=r.content
soup=BeautifulSoup(content,"html.parser")

page_number = soup.find_all("a",{"class":"Page"})[-1].text
base_url = "http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
full = []

for page in range(0,int(page_number)*10,10):
    print(base_url + str(page) + ".html")
    r=requests.get(base_url + str(page) + ".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    
    property_rows = soup.find_all("div",{"class":"propertyRow"})

    for property in property_rows:
        rows = {}
        rows["price"] = property.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

        rows["address"] = property.find_all("span",{"class":"propAddressCollapse"})[0].text
        rows["locality"] = property.find_all("span",{"class":"propAddressCollapse"})[1].text

        try:
            rows["beds"] = property.find("span",{"class":"infoBed"}).find("b").text
        except:
            rows["beds"] = None

        try:
            rows["area"] = property.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            rows["area"] = None

        try:
            rows["full baths"] =property.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            rows["full baths"] = None

        try:
            rows["half baths"] =property.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            rows["half baths"] = None

        for column_group in property.find_all("div",{"class":"columnGroup"}):        
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    rows["lot size"] = feature_name.text.replace(",","").replace(" ","")

        full.append(rows)
    

import pandas
df = pandas.DataFrame(full)
df.to_csv("output.csv")
