from ecdsa.numbertheory import inverse_mod
from random import randint
from Crypto.Util.number import *
from hashlib import sha256
from ecdsa import SECP256k1
from ecdsa.ecdsa import Public_key, Private_key, Signature
from pwn import *


E = SECP256k1
G, n = E.generator, E.order



r1 = 21781963780389728820678851448985592359690118674419650622762186914419240466217
s1 = 80272108699023689552645849001903286052885524335415423220786216770837881699879
r2 = 583249118905003460017748353118657627570175927985555445302813997666922803954
s2 = 66906535201216817475791316588898657219208059447656174835753633051780074614235
h1 = 1
h2 = 2
h1 = bytes_to_long(sha256(str(h1).encode()).digest())
h2 = bytes_to_long(sha256(str(h2).encode()).digest())

d_ans = (s1*h2-1337*s2*h1)*inverse_mod(1337*s2*r1-s1*r2, n) % n
k1 = (h1+d_ans*r1)*inverse_mod(s1, n) % n
k2 = k1 * 1337 % n
h = "Kuruwa"
h = bytes_to_long(sha256("Kuruwa".encode()).digest())

pubkey = Public_key(G, d_ans*G)
prikey = Private_key(pubkey, d_ans)

sig3 = prikey.sign(h, k2)
r3, s3 = sig3.r, sig3.s

print(r3,s3)

#FLAG{fcf8ab2bc7b42bbd00e5be2b3d311ec6e8a89526}
