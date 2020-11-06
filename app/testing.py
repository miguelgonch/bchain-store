from web3 import Web3 
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")                   # at the end point /

def main():                      
    w3 = Web3(Web3.WebsocketProvider("ws://127.0.0.1:8545"))
    w3.eth.defaultAccount = w3.eth.accounts[0]
    contract_address = "0xb994cbd783D1201F01E7B8FcB7145CFC7063693b"
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
    event1 = events[0]['args']
    return render_template("catalogue/catalogue.html",content=event1,title='Product')       


@app.route("/login")   
def login():
    return render_template("login.html")

if __name__ == "__main__":        
    app.run(debug=True)