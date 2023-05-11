# Import modules
import tools.addons.twilight.xor as Xor
import tools.addons.twilight.salt as Salt
import tools.addons.twilight.hash as Hash

# Encrypt function
def Encrypt(text, key):
    
    salt = Hash.getSaltByKey(key, text)
    saltedText = Salt.protect(text, salt)
    return Xor.encode(saltedText, key)

# Decrypt function
def Decrypt(text, key):
    unxoredText = Xor.decode(text, key)
    salt = Hash.getSaltByKey(key, unxoredText)
    return Salt.unprotect(unxoredText, salt)
