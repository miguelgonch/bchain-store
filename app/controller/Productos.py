import json
import hashlib
from config import abis
from config import configFile
from controller import contract
from Crypto.PublicKey import RSA


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
        accountId = 0
        print("No account found")
    #store_contract.functions.newProduct(hashh,_cantidad,_precio).transact()
    transactionStatus = contract.newProduct(hashh,_cantidad,_precio,accountId)
    if transactionStatus:
        pass
    else:
        print("Error")
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

def uploadkey(public, account):
    key = RSA.generate(2048)
    binPubKey =  key.publickey().exportKey('PEM')
    data = {'account':account,'pubKey':str(binPubKey)}
    result=db.keys.insert_one(data)
    #public={'publicK':public}
    #result=db.keys.insert_one(public)
    #public = {'key':str(public)}
    #result=db.keys.insert_one(public)
    public = str(public)

    #encripted = rsa.encrypt(b"This is the message to be encrypted", public)
    #key.decrypt(ast.literal_eval(str(encrypted)))

    # encrypted_message = rsa.encrypt(message, public_key)
    # decrypted_message = rsa.decrypt(encrypted_message, private_key)

#deleteProduct('28faaedf5071618129249db937bf59a1')
#prods = listProducts()
#hashh = createProduct('Oracle', 10, 'Licencia pirateada de OracleDB', 2, db)
#hashh = createProduct('Oracle', 10, 'Licencia pirateada de OracleDB', 2)