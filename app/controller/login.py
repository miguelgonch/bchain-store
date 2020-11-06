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

def importKeys(binPrivKey,binPubKey):
        # Key imports
    privKeyImp = RSA.importKey(binPrivKey)
    pubKeyImp =  RSA.importKey(binPubKey)

def getKeyObjects(privKeyImp,pubKeyImp):
    # Encryption objects
    privKeyObj = PKCS1_OAEP.new(privKeyImp)
    pubKeyObj = PKCS1_OAEP.new(pubKeyImp)

def encrypt(msg,pubKeyObj,privKeyObj):
    #msg = b'attack atdawn'
    emsg = pubKeyObj.encrypt(msg)
    dmsg = privKeyObj.decrypt(emsg)

def sign(msg,privKeyImp):
    # signature
    msg2 = b'attack at dawn'
    h = SHA256.new(msg2)
    signature = pss.new(privKeyImp).sign(h)
    
def verify(h,signature, pubKeyImp):
    # verification
    verifier = pss.new(pubKeyImp)
    try:
        verifier.verify(h, signature)
        print("The signature is authentic.")
    except (ValueError, TypeError):
        print("The signature is not authentic.")

# public key query
client = configFile.mongoClient
db = client.productos
query = db.keys.find_one({ "account": '0x9F460a9A5cC606E7cc20f586723E3DD3Ef6ec758' })
publicK = query['pubKey']
pubKeyImp =  RSA.importKey(publicK)

assert(msg == dmsg)