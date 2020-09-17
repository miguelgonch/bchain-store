pragma solidity ^0.5.10;

contract RequestProduct {
    mapping(address=>int) _productRequests;
    int _productPrice;
    int _productId;
    address _buyer = msg.sender;
    
    //event Pago(address buyer, address seller, int productId, int quantity);

    constructor(address seller, int productId, int expiration,int quantity) public {
        // Realizar la consulta para verificar la disponiblidad del producto (Para mientras es un > 0, luego hay que hacer consulta a la db y ver si existe el producto)
        int maxItems = 5;
        require(productId > 0,"Producto no es valido");
        require(0 < quantity && quantity < maxItems,"No es una cantidad valida, revisar unidades disponibles y pedido minimo");

        _productId = productId;
    }

    // funcion de aceptar request por parte del seller
    function sellerVote() public {
        
    }

    // Ok del buyer
    function buyerVote() public {
        // maxItems = consultar en db maximo dispobible

    }
}
