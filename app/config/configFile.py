from web3 import Web3
import pymongo
store_address = "0x9F0353A38c2CCB09d3440B6a7D85cb61d59e882E"
w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:9000"))
mongoClient = pymongo.MongoClient("mongodb+srv://dbUser:dbUser@cluster0.64zqb.mongodb.net/<dbname>?retryWrites=true&w=majority")