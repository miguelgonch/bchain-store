// const RequestProduct = artifacts.require("RequestProduct");

// module.exports = function (deployer) {
//   deployer.deploy(RequestProduct,"0x5b14089ED4366F823FD3b00513b2Afc820d041A1",2,5,1);
// };

const Store = artifacts.require("Store");

module.exports = function (deployer) {
  deployer.deploy(Store,"0x80E0C986934bda2d33C5620576518191aD53aCF1");
};