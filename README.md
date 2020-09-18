# Bchain-store
Proyecto blockchain: E-commerce utilizando blockchains

## Instrucciones
Disponible en: https://github.com/universidad-del-istmo/Blockchains-2020/tree/master/proyecto/


## Tienda Tehereum

### Compra de Licencia

* El merchant ha proveido al servicio una lista de licencias

1. El comprador publica un "mensaje de compra"
  1. Fondos reservados para la compra
  2. Fondos reservados para el fee de la plataforma
  3. Fecha de expiracion
    * Definida por el comprador
    * Definida por el servicio

2. El merchant publica mesaje de confirmacion

3. Como servicio publican que la licencia ha sido revelada

4. Se concluye el contrato y todos reciben su pago


### Comandos para prueba
* En truffle: Instanciar el contrato y probar la funcion con cierta cuenta y mandando cierta cantidad. El contrato esta instanciado por default en la cuenta indicada en migrations/2_RequestProduct.js, es necesario cambiarla a la cuenta del nuevo blockchain.
```
testing = await RequestProduct.deployed();
testing.buyerReserve({from: "Buyer Account Address", value: "35000000000000000000"})
```
* Verificar: Verificar el balance en la cuenta y en el contrato
```
web3.eth.getBalance("Buyer Account Address")
web3.eth.getBalance("Contract Address")
```
* Aceptar Contrato: Vendedor acepta el pago
```
testing.sellerAccept()
```


