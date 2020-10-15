const RequestProduct = artifacts.require("RequestProduct");

module.exports = function (deployer) {
  deployer.deploy(RequestProduct,"0x5b14089ED4366F823FD3b00513b2Afc820d041A1",2,5,1);
};
