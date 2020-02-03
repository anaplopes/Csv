from pymongo import MongoClient


class ConnectMongo:

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/') #conecta no banco de dados
        
    def connect_db(self, db, collection):
        self.client[db] #acessa o banco de dados
        session = db[collection] #acessa a minha coleção dentro desse banco de dados
        return session
