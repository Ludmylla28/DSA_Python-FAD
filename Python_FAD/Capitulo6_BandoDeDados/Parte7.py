print("Criando um Banco de Dados no MongoDB")
print("------------------------------------")
print("Gravando Dados no MongoDB com PyMongo")
print("-------------------------------------")

# Caso o PyMongo não esteja instalado, abra um prompt de comando e execute:
# pip install pymongo
# !pip install pymongo

# Importamos o MongoClient para conectar nossa aplicação ao MongoDB
from pymongo import MongoClient
# Estabelecemos a conexão ao Banco de Dados
conn = MongoClient('localhost', 27017)
type(conn)

# Uma única instância do MongoDB pode suportar diversos bancos de dados.
# Vamos criar o banco de dados cadastrodb
db = conn.cadastrodb
type(db)

# Uma coleção é um grupo de documentos armazenados no MongoDB
# (relativamente parecido com o conceito de tabelas em bancos relacionais)
collection = db.cadastrodb
type(collection)

import datetime

post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": datetime.datetime.utcnow()}

type(post1)
collection = db.posts
post_id = collection.insert_one(post1)
post_id.inserted_id

# Quando um documento é inserido uma chave especial, "_id", é adicionada
# automaticamente se o documento ainda não contém uma chave "_id".
post_id

post2 = {"codigo": "ID-2209876",
        "prod_name": "Televisor",
        "marcas": ["samsung", "panasonic", "lg"],
        "data_cadastro": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post2).inserted_id
post_id
collection.find_one({"prod_name": "Televisor"})

# A função find() retorna um cursor e podemos então navegar pelos dados
for post in collection.find():
    print(post)

# Verificando o nome do banco de dados
db.name

# Listando as coleções disponíveis
db.collection_names()
