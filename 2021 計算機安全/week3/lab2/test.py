#!/usr/bin/env python3
import os
import random
import sys
import string
from math import sin
from hashlib import sha256

USERS = {}
USERS[b'Admin'] = b'123'
USERS[b'Guest'] = b'No FLAG'


def MyHash(s):
    A = 0x10ee7647
    B = 0xb1b4fcd2
    C = 0x0c17fd4f
    D = 0x62e14c8c
    E = 0x36746fa0
    F = 0x9ad0cec5

    def G(X, Y, Z):
        return (X ^ (~Z | ~Y) ^ Z) & 0xFFFFFFFF

    def H(X, Y):
        return (X << Y | X >> (32 - Y)) & 0xFFFFFFFF

        
    X = [int((0xFFFFFFFE) * sin(i)) & 0xFFFFFFFF for i in range(256)]
    s_size = len(s)
    s += bytes([0x80])
    if len(s) % 128 > 120:
        while len(s) % 128 != 0:
            s += bytes(1)
    while len(s) % 128 < 120:
        s += bytes(1)
    s += bytes.fromhex(hex(s_size * 8)[2:].rjust(16, '0'))
    for i, b in enumerate(s):
        k, l = int(b), i & 0x1f
        A = (B + H(A + G(B, C, D) + X[k], l)) & 0xFFFFFFFF
        B = (C + H(B + G(C, D, E) + X[k], l)) & 0xFFFFFFFF
        C = (D + H(C + G(D, E, F) + X[k], l)) & 0xFFFFFFFF
        D = (E + H(D + G(E, F, A) + X[k], l)) & 0xFFFFFFFF
        E = (F + H(E + G(F, A, B) + X[k], l)) & 0xFFFFFFFF
        F = (A + H(F + G(A, B, C) + X[k], l)) & 0xFFFFFFFF

    return ''.join(map(lambda x: hex(x)[2:].rjust(8, '0'), [A, F, C, B, D, E]))


def verify(*stuff):
    return MyHash(b'&&'.join(stuff)).encode()


def main():
    username = input(
        'Welcome to our system!\nPlease Input your username: ').encode()
    if b'&' in username:
        print('nope')
        exit(-1)
    if username in USERS:
        password = USERS[username]
    else:
        password = input("Are you new here?\nLet's set a password: ").encode()
        USERS[username] = password

    print(f'Hello {username.decode()}')
    # session = bytes.hex(os.urandom(10)).encode()
    session = '11111111111111111111'.encode()
    print(f'Here is your session ID: {session.decode()}')
    print(
        f'and your MAC(username&&password&&sessionID): {verify(username,password,session).decode()}')

    while True:
        mac, * \
            sess, cmd = bytes.fromhex(
                input('\nWhat do you want to do? ')).split(b'&&')
        if mac == verify(username, password, *sess, cmd) and session in sess[0]:
            if cmd == b'flag':
                if username == b'Admin':
                    print("FLAG")
                    return
                else:
                    print('Permission denied')
            elif cmd == b'exit':
                print('exit')
                break
            else:
                print('Unknown command.')
        else:
            print('Refused!')
    print('See you next time.')


if __name__ == '__main__':
    main()
