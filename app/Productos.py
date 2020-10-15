import json
import hashlib
import pymongo

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

    descripcion = createDescription(_nombre, _precio, _descripcion)
    hashh = createDescriptionHash(descripcion)

    producto = {
    "hash": hashh,
    "cantidad": _cantidad,
    "descripcion": descripcion,
    }
    result=db.products.insert_one(producto)
    print(result)
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

def hi():
    print('Hello!!')
print('estas adentro!!!!')

#hashh = createProduct('OracleDB', 10, 'Licencia pirateada de OracleDB', 2, db)

#res = db.products.find_one({ "descripcion.nombre": "OracleDB" })
#print(res['hash'])
#if res['hash']==hashh:
#    print('yay')

#SendJSON
