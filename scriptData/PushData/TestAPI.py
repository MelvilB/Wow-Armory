import requests
import json
from pymongo import MongoClient
import json
client = MongoClient(
     "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
db = client.wow_test
cursor = db.data_player.find({"name":"Messi"})
# my_list=list(cursor)
# my_dict=my_list[0]
# my_dict.pop('_id')

# response = requests.get("http://api.open-notify.org/astros.json")
# print(response.json())
data = {
  'grant_type': 'client_credentials'
}

response = requests.post('https://us.battle.net/oauth/token', data=data, auth=('4e66ef876fe64f95955e1123a9a03bb7', 'YrEHs7S12Ufyn5mcnsAkYOVqIhtpYvx2'))
print(response.json())
reponseJSON=response.json()
#dict=json.loads(response)
access_token=reponseJSON['access_token']
#print(access_token)
r = requests.get(
    "https://us.api.blizzard.com/data/wow/media/playable-class/2?namespace=static-1.13.4_33598-classic-us")
print(r.json())

currently_equipped = my_dict['currently_equipped']
print(currently_equipped)
url_list = []
for elem in currently_equipped:
    if(elem=='-1'):
      print("Pas d'objet sur l'emplacement.")
      url="Defaut"
      url_list.append(url)
    else:
      r = requests.get(
        "https://us.api.blizzard.com/data/wow/media/item/" + elem + "?namespace=static-classic-us&locale=en_US&access_token=" + access_token)
      # print(r.json())
      apiResponse = r.json()
      url = apiResponse['assets'][0]['value']
      print("url: " + url)
      url_list.append(url)
#print(url_list)
my_dict['url_list']=url_list
print(my_dict)
