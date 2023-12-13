import pandas as pd
import requests


#Enter the link to Zannys google sheet doc below
SheetLink = "https://docs.google.com/spreadsheets/d/1hkuegpndWZqv4KeH_HC4SI8D-d6pvB95J2EwQZlLmaA/edit#gid=0"
#Enter the name of the faction
factionname = "Pennywise Clown Posse"

SheetLink = SheetLink.split('/ed')[0]
SheetLink = SheetLink .split("/d/")[1]
SheetLink = "https://docs.google.com/spreadsheet/ccc?key="+SheetLink+"&output=csv"
   
#YOUR_SHEET_ID='1hkuegpndWZqv4KeH_HC4SI8D-d6pvB95J2EwQZlLmaA'

r = requests.get(SheetLink)
open('dataset.csv', 'wb').write(r.content)

file1 = open(factionname+".json", "a")
startchar = ""
file1.writelines("{")

df = pd.read_csv('dataset.csv',header=1)

for index, row in df.iterrows():
    membername = row.Name
    stat = row['Stat Range'].split(' ')[1]
    profile = row['Profile Link'].split('=')[1]
    if stat == "Under":
        stat = "Under 2K"
    if stat == "200k-":
        stat = "200k- 2.5m"
    json= '''       
        "life_current": 0,
        "life_maximum": 0,
        "status_description": "",
        "status_details": "",
        "status_color": "",
        "status_state": "",
        "status_until": 0,
        "level": 11,
        "last_action_relative": "",
        "last_action_timestamp": 0,
        "last_action_status": "",
        "update_timestamp": 0,
        "last_attack_attacker": true,
        "last_attack_timestamp": 0,
        "note": "'''+stat+'''",
        "color": 0,
        "result": "",
        "fair_fight": 1.0,
        "flat_respect": 0,
        "base_respect": 0,
        "win": 0
    }'''
    memberjson = [startchar+'\n','"'+profile+'": {\n','"name": "'+membername+'",\n',json]
    file1.writelines(memberjson)
    startchar = ","

file1.writelines("}")
file1.close()
