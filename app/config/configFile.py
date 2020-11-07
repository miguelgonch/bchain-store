from web3 import Web3
import pymongo
store_address = "0x2e911bBbbeBBb07b9C18d1d1fFb3F0d7D6Ab40aa"
w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:9000"))
mongoClient = pymongo.MongoClient("mongodb+srv://dbUser:dbUser@cluster0.64zqb.mongodb.net/<dbname>?retryWrites=true&w=majority")