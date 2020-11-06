from web3 import Web3 
from flask import Flask,render_template, redirect, url_for, request
import Productos
from config import configFile
from config import abis

app = Flask(__name__)

# w3 and contract variables
w3 = Web3(Web3.WebsocketProvider(configFile.wsURL))
w3.eth.defaultAccount = w3.eth.accounts[0]
store_address = configFile.store_address
store_abi = abis.abi_store
storeContract = w3.eth.contract(address=store_address, abi=store_abi)

@app.route("/")                   # at the end point /
def main():                      
    
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
    
    return render_template("catalogue/catalogue.html",products=products,title='Product')       


@app.route("/login")   
def login():
    return render_template("login.html")

@app.route("/new-product")
def newProduct():
   return render_template("newproduct.html")

@app.route("/delete-product")
def deleteProduct():
   return render_template("deleteproduct.html")

@app.route("/add-product", methods = ['GET', 'POST'])
def newProductCon():
    producto = request.form['name']
    precio = int(request.form['precio'])
    descripcion = request.form['descripcion']
    cantidad = int(request.form['cantidad'])
    Productos.createProduct(producto,precio,descripcion,cantidad)
    return redirect(url_for('main'))

@app.route("/delete-prod", methods = ['GET', 'POST'])
def deleteProductCon():
    hashh = request.form['hash']
    Productos.deleteProduct(hashh)
    return redirect(url_for('main'))

    
if __name__ == "__main__":        
    app.run(debug=True)