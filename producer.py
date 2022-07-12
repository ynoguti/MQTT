from pymongo import MongoClient
import random
import datetime

mongo_client = MongoClient('localhost',27018)
mongo_db = mongo_client['teste']
mongo_collection = mongo_db['temperatura']

# Gerando temperatura
temp = int(random.uniform(10,45))

mensagem = {
    'data': datetime.datetime.now(),
    'temperatura': temp
}

# Guardando temperatura no MongoDB
mongo_collection.insert_one(mensagem)