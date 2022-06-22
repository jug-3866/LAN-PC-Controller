import requests
import json

url = "http://192.168.0.97:5000/"

data = { 'name': 'wow', 
         'Cse': 'haha' }

r = requests.post(url, data=json.dumps(data), headers={'Content-Type':'application/json'})

quit()