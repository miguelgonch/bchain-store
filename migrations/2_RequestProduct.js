const RequestProduct = artifacts.require("RequestProduct");

module.exports = function (deployer) {
  deployer.deploy(RequestProduct());
};
