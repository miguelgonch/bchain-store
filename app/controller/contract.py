from config import configFile
from config import abis
import sys

w3 = configFile.w3
w3.eth.defaultAccount = w3.eth.accounts[0]
store_address = configFile.store_address
store_abi = abis.abi_store
storeContract = w3.eth.contract(address=store_address, abi=store_abi)

def newProduct(prodHash,stockQuantity,price,accountId):
    try:
        storeContract.functions.newProduct(prodHash,stockQuantity,price).transact({'from': w3.eth.accounts[accountId]})
        return True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False
    