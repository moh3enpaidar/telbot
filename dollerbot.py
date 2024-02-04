import requests
import json
#site api http://api.navasan.tech
url = "http://api.navasan.tech/latest/?api_key=api"
r = requests.get(url)
js = json.loads(r.content)
dollar = []
msg = []
for k, v in js['usd'].items():
    dollar.append(v)

for i in dollar:
    msg.append(str(i))

token = 'bot token'
chatid = 'user id'
G = f"قیمت دلار: {msg[0]}"
SEND_TEXT = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&parse_mode=markdown&text={G}'

response = requests.get(SEND_TEXT)

