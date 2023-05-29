
import random
import hashlib

import random
import hashlib
from sympy.ntheory.modular import crt



flag = "c401549a04656914f9288164f6298ccc09771d8805db7248e3162b86237cefd2621df96509d8d9f32dbd2f56c6c41414971b990f31f80ced0cfe4eac89f55a93"
k = "5715730984776927122596830589662518107985433313538424944515197264212496003944524476815735435643637740104215871453370771557423444072451953725982027"

k = hashlib.sha512(str(k).encode('ascii')).digest()



flag=bytes.fromhex(flag)


enc = bytes(ci ^ ki for ci, ki in zip(flag.ljust(len(k), b'\0'), k))
print(enc)

#FLAG{0e8dc88cd3dc6717bf1e98126ccd295e559f9a03}