const RequestProduct = artifacts.require("RequestProduct");

module.exports = function (deployer) {
  deployer.deploy(RequestProduct,"0x3e0a39c5e8b68afb43d14b7a43a9e82ae37cb54f",2,5,1);
};
