from flask import Flask,render_template, redirect, url_for, request
from controller import Productos
from config import configFile
from config import abis

app = Flask(__name__)

# w3 and contract variables
w3 = configFile.w3
w3.eth.defaultAccount = w3.eth.accounts[0]
store_address = configFile.store_address
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
        title = ('Product: '+products[0][1]['descripcion']['nombre'])
    else:
        title = 'Not Found'

from config import configFile
from config import abis
import sys

w3 = configFile.w3
w3.eth.defaultAccount = w3.eth.accounts[0]
store_address = configFile.store_address
store_abi = abis.abi_store
storeContract = w3.eth.contract(address=store_address, abi=store_abi)
product_abi = abis.abi_product
prodHash = '503d16a924894a59c7d32a0e3953a293'
eventsFilter = storeContract.events.NewProduct.createFilter(fromBlock="0x0")
events = eventsFilter.get_all_entries()
actualStock = 0
for event in events:
    productAddress = event['args']['productAddress']
    producthash = event['args']['productHash']
    if producthash == prodHash:
        productContract = w3.eth.contract(address=productAddress, abi=product_abi)
        actualStock = productContract.functions._stock().call()
finalStock = actualStock    

import KeyGenerator

account = '0x9F460a9A5cC606E7cc20f586723E3DD3Ef6ec758'
keys = KeyGenerator.generateKeys()
public = keys[0]
puplicKeyInfo = [public.n,public.e]
private = keys[1]
privateKeyInfo = [private]

info = puplicKeyInfo
#Productos.uploadkey(keys[0],account)