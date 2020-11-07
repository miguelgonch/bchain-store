import json
import hashlib
#from config import abis
#from config import configFile
#from controller import contract
#from Crypto.PublicKey import RSA


w3 = configFile.w3
w3.eth.defaultAccount = w3.eth.accounts[0]
false=False

Store_address = configFile.store_address

store_contract = w3.eth.contract(address=Store_address, abi=abis.abi_store)
a = store_contract.functions

#Coneccion con la db

client = configFile.mongoClient
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
def createProduct(_nombre, _precio, _descripcion, _cantidad,_account):
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
    if _account:
        accountId = contract.getAccountId(_account)
    else:
        accountId = False
        print("No account found")
    #store_contract.functions.newProduct(hashh,_cantidad,_precio).transact()
    transactionStatus = contract.newProduct(hashh,_cantidad,_precio,accountId)
    if transactionStatus:
        return hashh
    else:
        print("Error")
        return False

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

def uploadkey(binPubKey, account):
    #data = {'account':account,'pubKey':str(binPubKey)}
    checkAccount = getKey(account)
    if not(checkAccount):
        data = {'account':account,'pubKey':(binPubKey)}
        result = db.keys.insert_one(data)
        if result:
            return True
        else:
            return False
    else:
        return False
def getKey(account):
    result = db.keys.find_one({"account":account})
    if result:
        return result['pubKey']
    else:
        return False

def reduceProductQuantity(_hash):
    #myquery = { "hash": _hash }
    myquery = { "hash": '71f2a4442cf3a4d7457e522f4d770980' }
    query = db.products.find_one(myquery)
    nuevaCantidad = int(query['cantidad']) - 1
    updateQuantity = { "$set": { "cantidad": nuevaCantidad } }
    db.products.update_one(myquery, updateQuantity)
    a=1

reduceProductQuantity('hashlib2')

