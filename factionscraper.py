import requests
#What faction ID would you like to scrape the members of?
factionid = "40774"
#Enter your API token here
APIToken = ""
Faction_url = "https://api.torn.com/faction/"+factionid+"?selections=basic&key="+APIToken
response = requests.get(Faction_url)
faction = response.json()
factionname = faction['name']
file1 = open(factionname+".json", "a")
startchar = ""
file1.writelines("{")


json= '''       "life_current": 0,
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
        "note": "",
        "color": 0,
        "result": "",
        "fair_fight": 1.0,
        "flat_respect": 0,
        "base_respect": 0,
        "win": 0
    }'''

#print (faction['members'])
#file1.writelines(faction['members'])
#file1.close()

for member in faction['members']:
    #print(faction['members'][member]['name'])
    membername = faction['members'][member]['name']
    memberjson = [startchar+'\n','"'+member+'": {\n','"name": "'+membername+'",\n',json]
    file1.writelines(memberjson)
    startchar = ","

file1.writelines("}")
file1.close()
