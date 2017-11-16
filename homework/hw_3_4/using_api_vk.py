import time
from itertools import combinations
import requests


AUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = '6258132'
VERSION = '5.69'

# auth_data = {
#     'client_id': APP_ID,
#     'redirect_uri': 'https://oauth.vk.com/blank.html',
#     'display': 'page',
#     'scope': 'friends',
#     'response_type': 'token',
#     'v': VERSION
# }
# print('?'.join(
#      (AUTH_URL, urlencode(auth_data))
# ))
TOKEN = '69f372b95e455f4a1bc1df7a9280789c3480eb8aaeade64dc3633ccb0e97c2575c327b02bd681f52119e7'
params = {
    'access_token': TOKEN,
    'v': VERSION
}

response = requests.get('https://api.vk.com/method/friends.get', params)
response_json = response.json()
friends_set = set(response_json['response']['items'])

list_friends_of_friends = [friends_set]

for friend_id in friends_set:
    time.sleep(0.15)

    params = {
        'access_token': TOKEN,
        'v': VERSION,
        'user_id': friend_id
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    response_json = response.json()
    if 'error' in response_json:
        continue

    friends_set = set(response_json['response']['items'])
    print(len(friends_set))
    list_friends_of_friends.append(friends_set)

comb_tup = combinations(list_friends_of_friends, 2)
mutual_friends = set()
for comb in comb_tup:
    mutual_friends.update(set.intersection(*comb))

print('Общие друзья всех друзей')
print(mutual_friends)
