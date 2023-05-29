from Crypto.Util.number import getPrime, inverse, bytes_to_long
import random
import math
import numpy as np

q=13198797472876287864902532913662133207745076880722933181850739256048248640200371699901863528719230289037546070463557840514069399741170318469168055220829673
h=10087945478419986810683355485899283062694316065852893531674190136106148631015543635096193003039720583579764280499310840409413968369520060566979727182282589
e=8989708726503367404715754689730782388959095528339234074784589050444870239608140046626770182336762701788963731736424741343914003600890982230995409715448250
v1=vector((1,h))
v2=vector((0,q))
while True:
    if v2.norm()<v1.norm():
        v1,v2=v2,v1
    m=round(v1*v2/(v1*v1))
    
    if m==0:
        break
    v2=v2-m*v1