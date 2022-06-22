#use this to send webhooks

import requests
import json
url = ""
#put your url or ip address here^

data = { 'name': 'wow', 
         'Cse': 'haha' }

r = requests.post(url, data=json.dumps(data), headers={'Content-Type':'application/json'})

quit()