// SPDX-License-Identifier: MG
pragma solidity >=0.6.0 < 0.8.0;

contract Store {
    // hash del producto => address contrato producto
    mapping(string => address) _products;
    // hash del producto => address propietario
    mapping(string => address) _productOwners;

    address payable public _admin;

    event NewProduct(string productHash, address productAddress);
    

    constructor(address payable admin) payable {
        _admin = admin;
    }

    function newProduct(string calldata productHash, uint stockQuantity, uint price) external {
        address owner = msg.sender;
        require(
            _products[productHash] == address(0),
            "Hash de producto invalido"
        );
        _productOwners[productHash] = owner;
        Product product = new Product(productHash, owner, stockQuantity,price,this);
        emit NewProduct(productHash, address(product));
    }
}

contract Product {
    address payable public _owner;
    // address cliente => cantidad
    mapping(address=>uint) _productRequests;
    string _productHash;
    uint _stock;
    uint public _price;
    Store _storeContract;
    address payable public _storeAddress;
    
    event NewRequest(address requestAddress);

    constructor(string memory productHash, address owner, uint stockQuantity, uint price,Store storeContract) payable{
        _owner = payable(owner);
        _productHash = productHash;
        _stock = stockQuantity;
        _storeContract = storeContract;
        _storeAddress = _storeContract._admin();
        _price = price;
    }

    function requestProduct(uint quantity) external payable{
        address buyer = msg.sender;
        require(_stock > 0,"Sorry, we are out of stock");
        require(_stock >= quantity,"We do not have enough products, try with a smaller quantity");
        require(msg.value==(_price*quantity),"Check the pricetag");
        _productRequests[buyer] = _productRequests[buyer] + quantity;
        Request request = new Request(_productHash,buyer,quantity,this);
        address(request).transfer(msg.value);
        emit NewRequest(address(request));
    }
    function updateProductRequest(address buyer, uint quantity) external{
        require(_stock > 0,"Sorry, we are out of stock");
        require(_stock >= quantity,"We do not have enough products");
        require(_productRequests[buyer] >= quantity,"Inconsistency");
        _productRequests[buyer]= _productRequests[buyer] - quantity;
        _stock = _stock - quantity;
    }
}

contract Request{
    address payable _buyer;
    address payable _owner;
    address payable _storeAddress;
    string _productHash;
    uint256 public _amountPayed;
    uint public _quantity;
    Product _productContract;
    
    fallback() external payable { 
    }
    receive() external payable{
    }

    constructor(string memory productHash, address buyer, uint quantity, Product productContract) payable{
        _buyer = payable(buyer);
        _owner = productContract._owner();
        _storeAddress = productContract._storeAddress();
        _productContract = productContract;
        _productHash = productHash;
        _quantity = quantity;
        _amountPayed = quantity * _productContract._price();

    }
    function acceptOffer() public{
        require(msg.sender == _owner,"You're not the seller");
        _productContract.updateProductRequest(_buyer,_quantity);
        _storeAddress.transfer(_amountPayed/100);       // fee 1%
        //_storeAddress.transfer(1*1e18);
        _owner.transfer(_amountPayed-(_amountPayed/100));
        selfdestruct(_owner);
    }
    function cancelOffer() public{
        require(msg.sender == _buyer,"You're not the buyer");
        selfdestruct(_buyer);
    }
}