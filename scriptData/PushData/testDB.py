from pymongo import MongoClient
import json
client = MongoClient(
     "mongodb+srv://Backend:wow_armory_tc_2020$€@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")

db = client.wow_db
# db.data_player.insert_one(
#     {"item": "canvas",
#      "qty": 100,
#      "tags": ["cotton"],
#      "size": {"h": 28, "w": 35.5, "uom": "cm"}})
cursor = db.data_player.find({"name":"Messi","raceID":"Humain","localizedFaction":"Alliance"})
my_list=list(cursor)
my_dict=my_list[0]
# my_dict.pop('_id')
print(my_dict)
# db.icons.delete_one({"name": my_dict['name']})
# db.icons.insert_one(my_dict) #insertion du dictionnaire dans la DB


# name=b'dfghjkl'
# print(name)
# print(name.decode('ascii'))