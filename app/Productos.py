import json
import hashlib
import pymongo
import abis
from web3 import Web3

w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8545"))
w3.eth.defaultAccount = w3.eth.accounts[0]
false=False

Store_address = "0xb634E8B98A7fc3022da023d37f0d778E28DF42c6"

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

def createProduct(_nombre, _precio, _descripcion, _cantidad, db):
    global store_contract
    descripcion = createDescription(_nombre, _precio, _descripcion)
    hashh = createDescriptionHash(descripcion)

    producto = {
    "hash": hashh,
    "cantidad": _cantidad,
    "descripcion": descripcion,
    }
    result=db.products.insert_one(producto)
    print(result)
    newProductFunction = store_contract.functions.newProduct(hashh,_cantidad,_precio).transact()
    return hashh

def checkHash(_hash):
    res = db.products.find_one({ "descripcion.nombre": "OracleDB" })
    print(res['hash'])
    if res['hash']==_hash:
        print('yay')    

def deleteProduct(_hash, db):
    result = db.products.delete_one({'hash': _hash})
    if result:
        print('Entrada Eliminada')

def findAll():
    result = db.products
    results = []
    for prods in result.find({}):
        results.append(prods)
    
    if results:
        return results

def hi():
    print('Hello!!')
print('estas adentro!!!!')

prodsData = findAll()
print(prodsData)    
hashh = createProduct('Oracle', 10, 'Licencia pirateada de OracleDB', 2, db)

#res = db.products.find_one({ "descripcion.nombre": "OracleDB" })
#print(res['hash'])
#if res['hash']==hashh:
#    print('yay')

#SendJSON
