from web3 import Web3 
from flask import Flask,render_template, redirect, url_for, request
import Productos
from config import abis

app = Flask(__name__)

# w3 and contract variables
w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:9000"))
w3.eth.defaultAccount = w3.eth.accounts[0]
store_address = "0x9cD5Eaef94D5c126C391D083F4c5F53da91747e8"
store_abi = abis.abi_store
storeContract = w3.eth.contract(address=store_address, abi=store_abi)
                   
    
#newProductFunction = storeContract.functions.newProduct("hash",13,5).transact()
eventsFilter = storeContract.events.NewProduct.createFilter(fromBlock="0x0")
events = eventsFilter.get_all_entries()
#receipt = w3.eth.getTransactionReceipt(newProductFunction)
#events = storeContract.events.NewProduct().processReceipt(receipt)
event1 = events[0]['args']
products = []
for event in events:
    prodInfo = Productos.checkHash(event['args']['productHash'])
    products.append([event,prodInfo])

eventsFilter = storeContract.events.NewProduct.createFilter(fromBlock="0x0")
hashVar='0b2d68d68ddb6fb6d0c5345dfe498083'
events = eventsFilter.get_all_entries()
products = []
for event in events:
    if event['args']['productHash'] == hashVar:
        prodInfo = Productos.checkHash(event['args']['productHash'])
        products.append([event,prodInfo])
var2 = products[0][1]['descripcion']['nombre']
var = 1