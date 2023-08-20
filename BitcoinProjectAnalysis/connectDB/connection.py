from pymongo import MongoClient

def connectDb():
    # Conectar ao MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['bitcoin']
    collection = db['bitcoinCollection']
    
    return collection