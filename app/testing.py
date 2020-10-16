from web3 import Web3 
from flask import Flask

app = Flask(__name__)

@app.route("/")                   # at the end point /

def main():                      # call method hello
    w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8545"))
    w3.eth.defaultAccount = w3.eth.accounts[0]
    contract_address = "0xC56cE9D9EC4074311d3DA8719b520d3Fa843c8e0"
    contract_abi = [
        {
            "inputs": [
                {"internalType": "address payable", "name": "admin", "type": "address"}
            ],
            "stateMutability": "payable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": False,
                    "internalType": "string",
                    "name": "productHash",
                    "type": "string",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "productAddress",
                    "type": "address",
                },
            ],
            "name": "NewProduct",
            "type": "event",
        },
        {
            "inputs": [],
            "name": "_admin",
            "outputs": [{"internalType": "address payable", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "string", "name": "productHash", "type": "string"},
                {"internalType": "uint256", "name": "stockQuantity", "type": "uint256"},
                {"internalType": "uint256", "name": "price", "type": "uint256"},
            ],
            "name": "newProduct",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ]
    myContract = w3.eth.contract(address=contract_address, abi=contract_abi)
    newProductFunction = myContract.functions.newProduct("hash",13,5).transact()

    receipt = w3.eth.getTransactionReceipt(newProductFunction)
    events = myContract.events.NewProduct().processReceipt(receipt)
    event1 = events[0]['args']['productAddress']
    return event1       # which returns "hello world"


if __name__ == "__main__":        # on running python app.py
    app.run()   