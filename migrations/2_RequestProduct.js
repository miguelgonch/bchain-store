const RequestProduct = artifacts.require("RequestProduct");

module.exports = function (deployer) {
  deployer.deploy(RequestProduct,"0x09a412ee2a12b4dba0446CCaD5a9FA4250e685F6",2,5,1);
};
