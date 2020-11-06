from web3 import Web3
import pymongo
store_address = "0x738B3296Ac03B3e185B3A80F9262967907b4689c"
w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:9000"))
mongoClient = pymongo.MongoClient("mongodb+srv://dbUser:dbUser@cluster0.64zqb.mongodb.net/<dbname>?retryWrites=true&w=majority")