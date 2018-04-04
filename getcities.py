import requests
import json, io



with open('key.txt','r') as f:
	key=f.readline().strip()

r=requests.get("https://www.numbeo.com/api/cities?api_key="+key)



with open('cities.json','w') as f:
	json.dump(r.json(),f,indent=4)