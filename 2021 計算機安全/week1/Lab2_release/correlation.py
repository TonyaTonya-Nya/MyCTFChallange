import itertools
import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random.random import getrandbits
import json

FLAG = b"FLAG{????????????????????????????????????????}"

ENC_FLAG = bytes.fromhex(
    "1e3c272c4d9693580659218739e9adace2c5daf98062cf892cf6a9d0fc465671f8cd70a139b384836637c131217643c1")


class LFSR:
    def __init__(self, key, taps):
        d = max(taps)
        assert len(key) == d, "Error: key of wrong size."
        self._s = key
        self._t = [d - t for t in taps]

    def _sum(self, L):
        s = 0
        for x in L:
            s ^= x
        return s

    def _clock(self):
        b = self._s[0]
        self._s = self._s[1:] + [self._sum(self._s[p] for p in self._t)]
        return b

    def getbit(self):
        return self._clock()


class Geffe:
    def __init__(self, key):
        # shard up 69+ bit key for 3 separate lfsrs
        assert key.bit_length() <= 19 + 23 + 27
        # convert int to list of bits
        key = [int(i) for i in list("{:069b}".format(key))]
        self.LFSR = [
            LFSR(key[:19], [19, 18, 17, 14]),
            LFSR(key[19:46], [27, 26, 25, 22]),
            LFSR(key[46:], [23, 22, 20, 18]),
        ]

    def getbit(self):
        b = [lfsr.getbit() for lfsr in self.LFSR]
        return b[1] if b[0] else b[2]


def encrypt_flag(key):
    sha1 = hashlib.sha1()
    sha1.update(str(key).encode('ascii'))
    key = sha1.digest()[:16]
    iv = bytes.fromhex('cd2832f408d1d973be28b66b133a0b5f')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(FLAG, 16))
    data = {}
    data['encrypted_flag'] = ciphertext.hex()

    return data


def decrypt_flag(key):  # 前19位元暴力
    sha1 = hashlib.sha1()
    sha1.update(str(key).encode('ascii'))
    key = sha1.digest()[:16]
    iv = bytes.fromhex('cd2832f408d1d973be28b66b133a0b5f')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ENC_FLAG)
    try:
        dec = plaintext.decode('ascii')
    except UnicodeDecodeError:
        return 'error'
    return dec


key = getrandbits(69)
J = Geffe(key)
stream = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1]


prime_key = [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0,
             1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]

s23 = ''
for i in prime_key:
    s23 += str(i)


ans = []

for i in range(pow(2, 20)-1):

    s = bin(i)[2:].zfill(19)
    s += s23
    dec = decrypt_flag(int(s, 2))

    if dec.find("error") == -1:
        ans.append(dec)

print(ans)
with open('ans.json', 'w') as f:
    f.write(json.dumps(ans, indent=1))


#key_len = 23
# for b in range(key_len):
#    print(b)
#    for c in itertools.combinations(range(key_len), b):
#
#        # i在c就反轉，否則輸出本身
#        key_candidate = [1-stream[i] if i in c else stream[i]
#                         for i in range(key_len)]
#        lfsr = LFSR(key_candidate, [23, 22, 20, 18])
#        s = [lfsr.getbit() for _ in range(256)]
#        matches = sum(a == b for a, b in zip(stream, s))
#        if matches >= 190:
#            joined_list = [*key_candidate, *prime_key]
#            print(key_candidate)


# 2 [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1]

# 3 [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]

# 2+3 [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
