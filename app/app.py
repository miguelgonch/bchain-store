from flask import Flask,render_template, redirect, url_for, request
from controller import Productos
from controller import contract
from controller import login as Login
from config import configFile
from config import abis
import KeyGenerator

app = Flask(__name__)

# w3 and contract variables
w3 = configFile.w3
w3.eth.defaultAccount = w3.eth.accounts[0]
store_address = configFile.store_address
store_abi = abis.abi_store
storeContract = w3.eth.contract(address=store_address, abi=store_abi)

@app.route("/")
@app.route("/products")                   # at the end point /
def main():                      
    eventsFilter = storeContract.events.NewProduct.createFilter(fromBlock="0x0")
    events = eventsFilter.get_all_entries()
    products = []
    content = ''
    for event in events:
        prodHash = event['args']['productHash']
        availableStock = contract.getProductStock(prodHash)
        if availableStock>0:
            prodInfo = Productos.checkHash(prodHash)
            products.append(prodInfo)
    if len(products) == 0:
        content = 'No hay productos disponibles'
    return render_template("catalogue/catalogue.html",products=products,content=content,title='Products')

@app.route("/products/<hashVar>")                   # at the end point /
def productInfo(hashVar):                      
    eventsFilter = storeContract.events.NewProduct.createFilter(fromBlock="0x0")
    events = eventsFilter.get_all_entries()
    products = []
    title = ''
    for event in events:
        if event['args']['productHash'] == hashVar:
            prodInfo = Productos.checkHash(event['args']['productHash'])
            products.append([event,prodInfo])
            title = ('Product: '+products[0][1]['descripcion']['nombre'])
        else:
            title = 'Not Found'

    return render_template("catalogue/product.html",products=products,title=title)       

@app.route("/login")   
def login():
    return render_template("login.html")

@app.route("/register")   
def register():
    return render_template("register.html")

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
    if 'account' in request.cookies:
        account = request.cookies.get['account']
    else:
        account = False
    Productos.createProduct(producto,precio,descripcion,cantidad,account)
    return redirect(url_for('main'))

@app.route("/delete-prod", methods = ['GET', 'POST'])
def deleteProductCon():
    hashh = request.form['hash']
    Productos.deleteProduct(hashh)
    return redirect(url_for('main'))

@app.route("/RSA-Generator",methods = ['POST'])
def generateRSA():
    if request.method == 'POST':
        account = request.form['account']
        keys = Login.createKeys()
        Productos.uploadkey(keys[1],account)
        return render_template(
            "giveKeys.html",
            public=keys[1],
            private=keys[0]
        )

    
if __name__ == "__main__":        
    app.run(debug=True)