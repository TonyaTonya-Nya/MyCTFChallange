from secrets import randbelow
M = 2**1024

def f(x):
    # this is a fast function
    return (4 * x**4 + 8 * x**8 + 7 * x**7 + 6 * x**6 + 3 * x**3 + 0x48763) % M

def encrypt(pt, key):
    ct = []
    for c in pt:
        ct.append(c ^ (key & 0xFF))
        key = 163
    return bytes(ct)

if __name__ == "__main__":
    key = randbelow(M)
    with open("./flag.txt", 'r') as f:
        flag = f.read()
    flag = bytes.fromhex(flag)
    print(encrypt(flag, key))