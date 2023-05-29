from pwn import *

r = remote('chals1.ais3.org', 12348)

r.recvline()
r.recvline()

for _ in range(0,25):
	response = r.recvline().decode()
	print(response)
	result = eval(response)
	print(result)
	r.send(str(result))

r.interactive()
