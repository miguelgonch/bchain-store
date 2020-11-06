import json
import hashlib
import pymongo
from config import abis
from web3 import Web3

w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:9000"))
w3.eth.defaultAccount = w3.eth.accounts[0]
false=False

Store_address = "0x09Fa82656A7E17075F3640F5e6C692C6E58167C8"

store_contract = w3.eth.contract(address=Store_address, abi=abis.abi_store)
a = store_contract.functions

#Coneccion con la db

client = pymongo.MongoClient("mongodb+srv://dbUser:dbUser@cluster0.64zqb.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.productos

#crear json de la descripcion del producto
def createDescription(_nombre, _precio, _descripcion):
    descripcion = {
    "nombre": _nombre,
    "precio": _precio,
    "descripcion": _descripcion,
    }
    return descripcion

def createDescriptionHash(_descripcion):
    bDescripcion = json.dumps(_descripcion, sort_keys = True).encode("utf-8")
    hashh = hashlib.md5(bDescripcion).hexdigest()
    return hashh

#def createProduct(_nombre, _precio, _descripcion, _cantidad, db):
def createProduct(_nombre, _precio, _descripcion, _cantidad):
    global store_contract, db
    descripcion = createDescription(_nombre, _precio, _descripcion)
    hashh = createDescriptionHash(descripcion)

    producto = {
    "hash": hashh,
    "cantidad": _cantidad,
    "descripcion": descripcion,
    }
    result=db.products.insert_one(producto)
    print(result)
    store_contract.functions.newProduct(hashh,_cantidad,_precio).transact()
    return hashh

def checkHash(_hash):
    query = db.products.find_one({ "hash": _hash })
    if query['hash']==_hash:
        return query   

def deleteProduct(_hash):
    global db
    result = db.products.delete_one({'hash': _hash})
    if result:
        print('Entrada Eliminada')

def hi():
    print('Hello!!')

def listProducts():
    query = db.products.find({})
    products = []
    for product in query:
        products.append(product)
    return products

#deleteProduct('28faaedf5071618129249db937bf59a1')
#prods = listProducts()
#hashh = createProduct('Oracle', 10, 'Licencia pirateada de OracleDB', 2, db)
#hashh = createProduct('Oracle', 10, 'Licencia pirateada de OracleDB', 2)