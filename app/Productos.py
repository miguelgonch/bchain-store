import json
import hashlib
import pymongo
import abis
from web3 import Web3

w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:9000"))
w3.eth.defaultAccount = w3.eth.accounts[0]
false=False

Store_address = "0xb634E8B98A7fc3022da023d37f0d778E28DF42c6"

# abi_product=[
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "string",
# 				"name": "productHash",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "address",
# 				"name": "owner",
# 				"type": "address"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "stockQuantity",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "price",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "contract Store",
# 				"name": "storeContract",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "payable",
# 		"type": "constructor"
# 	},
# 	{
# 		"anonymous": false,
# 		"inputs": [
# 			{
# 				"indexed": false,
# 				"internalType": "address",
# 				"name": "requestAddress",
# 				"type": "address"
# 			}
# 		],
# 		"name": "NewRequest",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "_owner",
# 		"outputs": [
# 			{
# 				"internalType": "address payable",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "_price",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "_storeAddress",
# 		"outputs": [
# 			{
# 				"internalType": "address payable",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "quantity",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "requestProduct",
# 		"outputs": [],
# 		"stateMutability": "payable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "buyer",
# 				"type": "address"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "quantity",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "updateProductRequest",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	}
# ]

# abi_store = [
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address payable",
# 				"name": "admin",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "payable",
# 		"type": "constructor"
# 	},
# 	{
# 		"anonymous": false,
# 		"inputs": [
# 			{
# 				"indexed": false,
# 				"internalType": "string",
# 				"name": "productHash",
# 				"type": "string"
# 			},
# 			{
# 				"indexed": false,
# 				"internalType": "address",
# 				"name": "productAddress",
# 				"type": "address"
# 			}
# 		],
# 		"name": "NewProduct",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "_admin",
# 		"outputs": [
# 			{
# 				"internalType": "address payable",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "string",
# 				"name": "productHash",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "stockQuantity",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "price",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "newProduct",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	}
# ]

# abi_request= [
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "string",
# 				"name": "productHash",
# 				"type": "string"
# 			},
# 			{
# 				"internalType": "address",
# 				"name": "buyer",
# 				"type": "address"
# 			},
# 			{
# 				"internalType": "uint256",
# 				"name": "quantity",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "contract Product",
# 				"name": "productContract",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "payable",
# 		"type": "constructor"
# 	},
# 	{
# 		"stateMutability": "payable",
# 		"type": "fallback"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "_amountPayed",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "_quantity",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "acceptOffer",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "cancelOffer",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"stateMutability": "payable",
# 		"type": "receive"
# 	}
# ]
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

def hi():
    print('Hello!!')
print('estas adentro!!!!')

hashh = createProduct('Oracle', 10, 'Licencia pirateada de OracleDB', 2, db)

#res = db.products.find_one({ "descripcion.nombre": "OracleDB" })
#print(res['hash'])
#if res['hash']==hashh:
#    print('yay')

#SendJSON
