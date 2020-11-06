from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from config import configFile

def createKeys():
    key = RSA.generate(2048)
    # Key creation
    binPrivKey = key.exportKey('PEM')
    binPubKey =  key.publickey().exportKey('PEM')
    return binPrivKey,binPubKey

def importKeys(binPrivKey,binPubKey):
    # Key imports
    privKeyImp = RSA.importKey(binPrivKey)
    pubKeyImp =  RSA.importKey(binPubKey)
    return privKeyImp,pubKeyImp

def getKeyObjects(privKeyImp,pubKeyImp):
    # Encryption objects
    privKeyObj = PKCS1_OAEP.new(privKeyImp)
    pubKeyObj = PKCS1_OAEP.new(pubKeyImp)
    return privKeyObj,pubKeyObj

def encrypt(msg,pubKeyObj):
    #msg = b'attack atdawn'
    emsg = pubKeyObj.encrypt(msg)
    return emsg

def decrypt(emsg,privKeyObj):
    dmsg = privKeyObj.decrypt(emsg)
    return dmsg

def sign(msg,privKeyImp):
    # signature
    msg = b'attack at dawn'
    h = SHA256.new(msg)
    signature = pss.new(privKeyImp).sign(h)
    return signature
    
def verify(h,signature, pubKeyImp,accoundAddress):
    # verification
    verifier = pss.new(pubKeyImp)
    try:
        verifier.verify(h, signature)
        print("The signature is authentic.")
        return True
    except (ValueError, TypeError):
        print("The signature is not authentic.")
        return False
    

# public key query
client = configFile.mongoClient
db = client.productos
query = db.keys.find_one({ "account": '0x9F460a9A5cC606E7cc20f586723E3DD3Ef6ec758' })
publicK = query['pubKey']
pubKeyImp =  RSA.importKey(publicK)

assert(msg == dmsg)