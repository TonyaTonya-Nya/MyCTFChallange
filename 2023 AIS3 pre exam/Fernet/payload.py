import os
import base64
from cryptography.fernet import Fernet
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import PBKDF2

s = "iAkZMT9sfXIjD3yIpw0ldGdBQUFBQUJrVzAwb0pUTUdFbzJYeU0tTGQ4OUUzQXZhaU9HMmlOaC1PcnFqRUIzX0xtZXg0MTh1TXFNYjBLXzVBOVA3a0FaenZqOU1sNGhBcHR3Z21RTTdmN1dQUkcxZ1JaOGZLQ0E0WmVMSjZQTXN3Z252VWRtdXlaVW1fZ0pzV0xsaUM5VjR1ZHdj"
s_decode = base64.b64decode(s.encode())
salt = s_decode[:16]
enc = s_decode[16:]

password = 'mysecretpassword'

def decrypt(ciphertext, password):
    key = PBKDF2(password.encode(), salt, 32,
                 count=1000, hmac_hash_module=SHA256)
    f = Fernet(base64.urlsafe_b64encode(key))
    plaintext = f.decrypt(enc)
    return plaintext


print(decrypt(enc, password))
