pragma solidity ^0.5.10;

contract RequestProduct {
    int _productPrice;
    int _productId;
    address _buyer = msg.sender;
    address public _seller;
    bool _paymentCompleted = false;

    //event Pago(address buyer, address seller, int productId, int quantity);

    constructor(
        address seller,
        int productId,
        int expiration,
        int quantity
    ) public {
        _seller = seller;
        
        // maxItems = consultar en db maximo dispobible
        int maxItems = 5;
        // Realizar la consulta para verificar la disponiblidad del producto (Para mientras es un > 0, luego hay que hacer consulta a la db y ver si existe el producto)
        require(productId > 0, "Producto no es valido");
        require(
            0 < quantity && quantity < maxItems,
            "No es una cantidad valida, revisar unidades disponibles y pedido minimo"
        );

        _productId = productId;
        // Consultar el precio del producto en la db
        _productPrice = 35;
    }

    // funcion de aceptar request por parte del seller
    function sellerAccept() public {}

    // Ok del buyer
    function buyerReserve()  external payable {
        require(int(msg.value) == _productPrice,'Not enough ether');
        //_buyer.transfer(_productPrice);
    }
}
