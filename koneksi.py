from pymongo import MongoClient
client = MongoClient('mongodb+srv://ezharya86:sparta@cluster0.vfirzon.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name':'bob',
    'age':27
}

db.users.insert_one(doc)