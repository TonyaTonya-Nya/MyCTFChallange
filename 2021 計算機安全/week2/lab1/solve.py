from pwn import *
from Crypto.Util.number import *

r = remote('edu-ctf.csie.org', 42071)

q = r.recvline()
n = int(q[4:])
q = r.recvline()
c = int(q[4:])

e = 2 ** 16+1

a = inverse(3, n)
m, b, i, f = 0, 0, 0, 0

while 1:
    r.sendline(str(pow(a, i*e, n)*c % n).encode())
    q = r.recvline()
    mm = (int(q.split()[-1])-(a*b) % n) % 3
    if mm == 0:
        f += 1
        if f == 10:
            break
    else:
        f = 0
    b = (a*b+mm) % n
    m = 3**i*mm+m
    i += 1

print(m)
print(long_to_bytes(m))

# FLAG{fcf8ab2bc7b42bbd00e5be2b3d311ec6e8a89526}