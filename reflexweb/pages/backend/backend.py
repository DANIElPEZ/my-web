from pymongo import MongoClient

client=MongoClient('your mongo host')
db=client['comments']
collection=db['comment']

async def insertar(name:str,text:str):
    document={
        'nombre':name,
        'texto':text
        }
    collection.insert_one(document)

async def buscar():
    asw=collection.find()
    return asw