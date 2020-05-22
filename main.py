import json
import requests

api_key = '' # your pubg api key here

headers = {'Authorization': 'Bearer {0}'.format(api_key), 'Accept' : 'application/vnd.api+json'} # headers used for the request

not_searching = True

while not_searching:
    print('please enter the platform you play on (pc-eu for example)')
    platform = input()
    print('please enter the players name')
    name = input()
    api_url = 'http://api.pubg.com/shards/' + platform + '/players?filter[playerNames]=' +  name
    response = requests.get(api_url, headers=headers)

    if(response.status_code == 200): # everything ok
        jsonresponse = json.loads(response.content.decode('utf-8'))
        account_id = jsonresponse['data'][0]['id'] # get players account id from json
        print(account_id) # print players account id
        not_searching = False
    else:
        print(str(response.status_code) + ' invalid request. check player name and platform' )
        not_searching = True
