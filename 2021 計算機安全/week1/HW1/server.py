#!/bin/env python3 -u
from sympy import Symbol, Poly

# state = int.from_bytes(os.urandom(8), 'little') # 亂數
poly = 0b1010101000001101001110100110011101111110000110111110000010111111
state= 0b1100110111001110101101111000101001001001000101111111100111111100
#poly = 0b1110
#state = 0b1010

'''
MAX=4
poly_list = [str(d) for d in str(bin(poly))[2:]]
print(poly_list)
P = ''
for i in range(0, MAX):
    if(poly_list[(MAX-1)-i]=='1'):
        P = P +'+x^'+str((MAX-1)-i)
print(P[1:])
'''

# 往右一個位元 輸出b0
# b0 是 1 則全體 xor poly
# b0 是 0 則 b4 是 0

# 對所有位元

# (b0 AND poly) xor state
# 最低位元是b0 最高是bn
# bn = (b0 AND 1) xor 0
# bn = b0

# 關鍵
# bn-1 = bn xor (b0 AND poly n-1)
# bn=(b0 AND poly n) Xor 0


def step():
    global state
    out = state & 1  # 對最低位元AND運算
    state >>= 1  # 捨棄最低位元 (/2向上取整)

    if out:  # 最低位元是1
        state ^= poly  # 獲得state/poly的餘數

    return out


def random():
    for _ in range(42):
        step()
    return step()


arr = []

money = 1.2
while money > 0:
    y = random()  # 傳回第43次
    #y=step()
    # x = int(input('> '))
    x = 1
    if x == y:
        money += 0.02
        arr.append(x)
    else:
        money -= 0.04
        arr.append(x ^ 1)

    # print(money)
    
    if money > 2.4:
        exit(0)

print(arr)

