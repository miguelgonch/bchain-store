import rsa

def generateKeys():
    public_key, private_key = rsa.newkeys(48)
    return public_key, private_key
