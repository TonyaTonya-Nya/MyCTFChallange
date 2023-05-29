#!/bin/env python3
import string
import hashlib


# key
with open('key.txt') as f:
    key = f.read().strip().split(' ')

# 字元集
charset = string.ascii_lowercase+string.digits+',. '
charset_idmap = {e: i for i, e in enumerate(charset)}

# 解凱薩
def decrypt(ctx, key):
    N, ksz = len(charset), len(key)
    return ''.join(charset[(c-int(key[i % ksz])) % N] for i, c in enumerate(ctx))


with open('./output.txt') as f:
    ctx = f.readline().strip()[4:]
    enc = bytes.fromhex(f.readline().strip()[6:])
ctx = [charset_idmap[c] for c in ctx]


with open("flag.txt", 'r') as f:
    flag = f.read()

flag = bytes.fromhex(flag)
k = hashlib.sha512(''.join(charset[int(k)]
                   for k in key).encode('ascii')).digest()
enc = bytes(ci ^ ki for ci, ki in zip(flag.ljust(len(k), b'\0'), k))


print(decrypt(ctx, key))
print(enc)
