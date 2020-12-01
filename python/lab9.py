import json
import requests



r = requests.get('http://localhost:3000')



data = r.json()

##print(data)

for d in data:
    print(d["name is"] + d["color"])
