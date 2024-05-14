import requests
import json

URL = 'https://api.twitch.tv/v5/videos/1422036330/comments?content_offset_second=0'
params = {}
params['client_id'] = '1cu75bp9ugj3q0fu7j8s5wzw7jcia8'
response = requests.get(URL, params=params)
#response.status_code
#MyPrettyPrinter().pprint(response.text)

j = json.loads(response.text)
print(j)
# print(j['_next'])
# print(j['comment'][0]['content_offset_seconds'])
# print(j['comment'][0]['message']['body'])