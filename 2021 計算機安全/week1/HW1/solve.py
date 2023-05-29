from pwn import *

r = remote('140.112.31.97', 42069)

a=1.20
arr=[]
for i in range(0,64):
    r.send(b'1\n')
    r.recvuntil('>')
    
    f=float(r.recvline(keepends=False))

    if f<a:
        arr.append(0)
    else :
        arr.append(1)
    a=f

print(arr)
r.interactive() 



