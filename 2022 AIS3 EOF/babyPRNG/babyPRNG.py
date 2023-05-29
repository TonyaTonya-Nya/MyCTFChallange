import random
import string

charset = string.ascii_letters + string.digits + '_{}'

class MyRandom:
    def __init__(self):
        self.n = 2**256
        self.a = random.randrange(2**256)
        self.b = random.randrange(2**256)

    def _random(self):
        tmp = self.a
        self.a, self.b = self.b, (self.a * 69 + self.b * 1337) % self.n
        tmp ^= (tmp >> 3) & 0xde
        tmp ^= (tmp << 1) & 0xad
        tmp ^= (tmp >> 2) & 0xbe
        tmp ^= (tmp << 4) & 0xef
        return tmp

    def random(self, nbit):
        return sum((self._random() & 1) << i for i in range(nbit))

random_sequence = []
for i in range(6):
    rng = MyRandom()
    random_sequence += [rng.random(8) for _ in range(10)]

print(random_sequence)


flag = bytes.fromhex(
    '9dfa2c9ccd5c84c61feb00ea835e848732ac8701da32b5865a84db59b08532b6cf32ebc10384c45903bf860084d018b5d55a5cebd832ef8059ead810')


ciphertext = bytes([x ^ y for x, y in zip(flag, random_sequence)])

print(bytes(ciphertext))

#FLAG{1_pr0m153_1_w1ll_n07_m4k3_my_0wn_r4nd0m_func710n_4641n}