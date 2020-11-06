from web3 import Web3
import pymongo
store_address = "0x9cD5Eaef94D5c126C391D083F4c5F53da91747e8"
w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:9000"))
mongoClient = pymongo.MongoClient("mongodb+srv://dbUser:dbUser@cluster0.64zqb.mongodb.net/<dbname>?retryWrites=true&w=majority")