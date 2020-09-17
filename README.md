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
* En truffle:
```
testing = await RequestProduct.deployed();
testing.buyerReserve({from: "0x3E0A39C5e8B68afb43D14b7a43A9e82Ae37cb54f", value: "35000000000000000000"})
web3.eth.getBalance("0x3E0A39C5e8B68afb43D14b7a43A9e82Ae37cb54f")
web3.eth.getBalance("0xf6bef30ccbf4628dd99fc1f87ea50d80740819b0")
```

