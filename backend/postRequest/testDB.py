from pymongo import MongoClient
import json
client = MongoClient(
     "mongodb+srv://dbUser2:dbUser2@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
db = client.wow_test
cursor = db.icons.find({"name":"Banzai"})
my_list=list(cursor)
my_dict=my_list[0]
my_dict.pop('_id')
print(my_dict)
my_json = json.dumps(my_dict)
print(my_json)

# name=b'dfghjkl'
# print(name)
# print(name.decode('ascii'))