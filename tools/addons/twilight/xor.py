# Import modules
from base64 import b64encode
from base64 import b64decode

# Xor
def xor(text, key):
    return ''.join(
        chr(ord(text[i]) ^ ord(key[i % len(key)])) for i in range(len(text))
    )

# Encode : [text => xor => base64]
def encode(text, key):
    return b64encode(xor(text, key).encode("utf-8")).decode()

# Decode : [xor => base64 => text]
def decode(text, key):
    return xor(b64decode(text).decode(), key)
