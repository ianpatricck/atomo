import pymongo
import json
import os

from dotenv import dotenv_values

config = dotenv_values(".env")

# Parametros de configuração da conexão com o MongoDB

DB_USER = config["DB_USER"] or os.getenv("DB_USER")
DB_PASS = config["DB_PASS"] or os.getenv("DB_PASS")
DB_CLUSTER = config["DB_CLUSTER"] or os.getenv("DB_CLUSTER")

# Conexão com o MongoDB
client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_CLUSTER}/?retryWrites=true&w=majority")

# Instancia do banco de dados a ser usada por alguns 'providers'
database = client["atomo"]

