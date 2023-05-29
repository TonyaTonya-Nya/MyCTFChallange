#!/usr/bin/env python3
from random import randint
from Crypto.Util.number import *
from hashlib import sha256, md5
from ecdsa import SECP256k1
from ecdsa.ecdsa import Public_key, Private_key, Signature

#FLAG = open("flag", 'r').read()

E = SECP256k1
G, n = E.generator, E.order

d=72916376899470629947371931744970385370825029776518713566146403077311000472052

pubkey = Public_key(G, d*G)
prikey = Private_key(pubkey, d)
print(f'P = ({pubkey.point.x()}, {pubkey.point.y()})')

# x=65823956811073419305151658063701250828042169631002777445968442385646872084469
# y=78326687082098639545880831244409056780207256799142459723325879429561430124098

# 1
# (2550747747040499505300640205848405970163613907458178216679568509625108287135, 109041362216927226499533668409725543479084342153568368043609752218525115930317)
# 2
# (72041870591058890304504668876849666543496824475191974671305535910201008445979, 83946795277792838980402202609676564717829063556370117046498421048868966186170)
# 3
# (108685330908277280820447057302718465017119108263834406240608091667595934616693, 98159137531445683172652018683410862274728682897960980275194154780437965482294)


for _ in range(3):
    print('''
1) talk to Kuruwa
2) login
3) exit''')
    option = input()
    if option == '1':
        msg = input('Who are you?\n')
        if msg == 'Kuruwa':
                print('No you are not...')
        else:
            h = sha256(msg.encode()).digest()
            k = int(md5(b'secret').hexdigest() + md5(long_to_bytes(prikey.secret_multiplier) + h).hexdigest(), 16)
            sig = prikey.sign(bytes_to_long(h), k)
            print(f'({sig.r}, {sig.s})')

    elif option == '2':
        msg = input('username: ')
        r = input('r: ')
        s = input('s: ')
        h = bytes_to_long(sha256(msg.encode()).digest())
        verified = pubkey.verifies(h, Signature(int(r), int(s)))
        if verified:
            if msg == 'Kuruwa':
                print("FLAG")
            else:
                print('Bad username')
        else:
            print('Bad signature')
    else:
        break
