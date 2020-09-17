pragma solidity ^0.5.10;

contract RequestProduct {
    mapping(address=>int) _productRequests;
    int _productPrice;
    int _productId;
    

    constructor(address buyer, int productId, int expiracion) public {
        // Realizar la consulta para verificar la disponiblidad del producto (Para mientras es un > 0, luego hay que hacer consulta a la db y ver si existe el producto)
        require(productId > 0,"Producto no es valido");

        _productId = productId;
    }

    function purchase(int quantity) public {
        // maxItems = consultar en db maximo dispobible
        int maxItems = 5;
        require(0 < quantity && quantity < maxItems,"No es una cantidad valida, revisar unidades disponibles y pedido minimo");
    }
}
