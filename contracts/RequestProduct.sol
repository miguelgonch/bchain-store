pragma solidity ^0.5.10;

contract RequestProduct {
    uint256 _productPrice;
    int256 _productId;
    //address payable _buyer = msg.sender;
    address payable _seller;
    bool _paymentCompleted = false;

    //event Pago(address buyer, address seller, int productId, int quantity);

    constructor(
        address payable seller,
        int256 productId,
        int256 expiration,
        int256 quantity
    ) public {
        _seller = seller;

        // maxItems = consultar en db maximo dispobible
        int256 maxItems = 5;
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
    function sellerAccept(address payable recipient) external payable {
        recipient.transfer(cantidad);
    }

    // Ok del buyer
    function buyerReserve() external payable {
        //require(msg.value >= _productPrice, "Not enough ether for purchase");
        //_buyer.transfer(_productPrice);
        //require(msg.value == _productPrice,'Not enough ether');
        //_seller.transfer(80);
    }

}
