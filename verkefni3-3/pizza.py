import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='YYZP11OZXDGHBC2IXXNM2OXZX1HTKPFK5MV5UKAHS5W35WQE',
  client_secret='1CKJT5PFJELQOMB3NWUD3PYQWEG1QRH4M4WIVJKBKZBO5DT2',
  v='20170801',
  ll='64.126521,-21.817439',
  query='pizza'
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
for x in data["response"]["groups"]:
    for y in x["items"]:
      if "city" in y["venue"]["location"]:
        if y["venue"]["location"]["city"]=="Reykjavík":
          print(y["venue"]["name"],y["venue"]["location"]["city"])