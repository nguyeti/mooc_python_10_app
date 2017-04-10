import folium as f, pandas as p

df = p.read_csv("Volcanoes-USA.txt")
df["DETAILS"] = 'name: ' + df["NAME"] +', status:' + df["STATUS"] + ', type: ' + df["TYPE"]
map = f.Map(location = [df["LAT"].mean(), df["LON"].mean()], zoom_start = 5)

def color(elev):
    min_elev = int(min(df["ELEV"]))
    step = int((max(df["ELEV"])-min(df["ELEV"]))/4)
    if elev in range(min_elev, min_elev + step):
        col = 'green'
    elif elev in range(min_elev + step, min_elev + step*2):
        col = 'yellow'
    elif elev in range(min_elev + step*2, min_elev + step*3):
        col = 'orange'
    else:
        col = 'red'
    return col

fg = f.FeatureGroup(name = "Volcanoes Locations")

for lat, lon, details,elev in zip(df["LAT"], df["LON"], df["DETAILS"], df["ELEV"]):
    # print(lat,lon,details)
    fg.add_child(f.Marker(location = [lat, lon], popup = f.Popup(details),icon = f.Icon(color = color(elev))))


map.add_child(fg)
map.add_child(f.LayerControl())
map.save("volcanoes.html")
