from pwn import *
from ecdsa import SECP256k1
from ecdsa.ecdsa import *
import random
from hashlib import sha256
from Crypto.Util.number import *
from ecdsa.numbertheory import inverse_mod


r = remote('140.112.31.97', 42072)

r.send(b'1\n')
r.send(b'1\n')
r.send(b'1\n')
r.send(b'2\n')

r.send(b'2\n')
r.send(b'Kuruwa\n')

r.interactive() 


'''
E = SECP256k1
G, n = E.generator, E.order
#d = random.randrange(1, n)
d = 57042573091656172859758137846927150587037425175174054704849289217138176158026
#print("D=", d)

pubkey = Public_key(G, d*G)
prikey = Private_key(pubkey, d)

h1 = 1
h2 = 2
#k = random.randrange(1, n)
k = 46568677541009366352459952166143728510512179791779229011690452369669806335633
#print("K=", k)

h1 = bytes_to_long(sha256(str(h1).encode()).digest())
sig1 = prikey.sign(h1, k)
r1, s1 = sig1.r, sig1.s
#print(f'sig1 = ({r1}, {s1})')


h2 = bytes_to_long(sha256(str(h2).encode()).digest())
k = k * 1337 % n
sig2 = prikey.sign(h2, k)
r2, s2 = sig2.r, sig2.s
#print(f'sig2 = ({r2}, {s2})')


d_ans = (s1*h2-1337*s2*h1)*inverse_mod(1337*s2*r1-s1*r2, n) % n
k1 = (h1+d_ans*r1)*inverse_mod(s1, n) % n
k2 = k1 * 1337 % n


h = "Kuruwa"
h = bytes_to_long(sha256("Kuruwa".encode()).digest())
sig3 = prikey.sign(h, k2)

r3, s3 = sig3.r, sig3.s

verified = pubkey.verifies(h, Signature(int(r3), int(s3)))

print(verified)
'''