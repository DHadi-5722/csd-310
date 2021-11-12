from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.j2vkp.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print("-- pytech collection list --")
print(db.list_collection_names())
