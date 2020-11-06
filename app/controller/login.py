from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from config import configFile

key = RSA.generate(2048)

# Key creation
binPrivKey = key.exportKey('PEM')
binPubKey =  key.publickey().exportKey('PEM')

# Key imports
privKeyImp = RSA.importKey(binPrivKey)
pubKeyImp =  RSA.importKey(binPubKey)

# Encryption objects
privKeyObj = PKCS1_OAEP.new(privKeyImp)
pubKeyObj = PKCS1_OAEP.new(pubKeyImp)

msg = b'attack at dawn'
emsg = pubKeyObj.encrypt(msg)
dmsg = privKeyObj.decrypt(emsg)

# signature
msg2 = b'attack at dawn'
h = SHA256.new(msg2)
signature = pss.new(privKeyImp).sign(h)

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
pubKeyImp =  RSA.importKey(binPubKey)

assert(msg == dmsg)