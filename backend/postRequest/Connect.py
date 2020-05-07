from pymongo import MongoClient
#import dnspython

client=MongoClient("mongodb+srv://dbUser2:dbUser2@cluster0-ll4tc.mongodb.net/test?retryWrites=true&w=majority")
db=client.sample_analytics
db.accounts.insert_one({ 'y_offset': dict['y_offset']})