from config import configFile
from config import abis
from controller import Productos
import sys

w3 = configFile.w3
w3.eth.defaultAccount = w3.eth.accounts[0]
store_address = configFile.store_address
store_abi = abis.abi_store
storeContract = w3.eth.contract(address=store_address, abi=store_abi)
product_abi = abis.abi_product
request_abi = abis.abi_request

def newProduct(prodHash,stockQuantity,price,accountId):
    try:
        storeContract.functions.newProduct(prodHash,stockQuantity,price).transact({'from': w3.eth.accounts[accountId[0]]})
        return True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False
def getAccountId(address):
    accountsTemp = w3.eth.accounts
    matchAccount = []
    i = 0
    for account in accountsTemp:
        if address == account:
            matchAccount.append([i,account])
        i = i + 1
    return matchAccount[0]

def getProductStock(prodHash):
    eventsFilter = storeContract.events.NewProduct.createFilter(fromBlock="0x0")
    events = eventsFilter.get_all_entries()
    actualStock = 0
    for event in events:
        productAddress = event['args']['productAddress']
        producthash = event['args']['productHash']
        if producthash == prodHash:
            productContract = w3.eth.contract(address=productAddress, abi=product_abi)
            actualStock = productContract.functions._stock().call()
    return actualStock

def createProductRequest(productAddress, account, costo):
    productContract = w3.eth.contract(address=productAddress, abi=product_abi)
    productContract.functions.requestProduct(1).transact({'from': account,'value': int(costo)})
    
    