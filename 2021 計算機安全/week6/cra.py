import Crypto.Util.number as c
a=1677936292368545917814039483235622978551357499172411081065325777729488793550136568309923513362117687939170753313352485633354858207097035878077942534451467
b=5687468800624594128838903842767411040727750916115472185196475570099217560998907467291416768835644005325105434981167565207313702286530912332233402467314947
m=1244793456976456877170839265783035368354692819005211513409129011314633866460250237897970818451591728769403864292158494516440464466254909969383897236264921
n=198148795890507031730221728469492521085435050254010422245429012501864312776356522213014006175424179860455397661479243825590470750385249479224738397071326661046694312629376866307803789411244554424360122317688081850938387121934893846964467922503328604784935624075688440234885261073350247892064806120096887751
e=65537

enc_long=48071438195829770851852911364054237976158406255022684617769223046035836237425012457131162001786019505606941050117178190535720928339364199078329207393922570246678871062386142183424414041935978305046280399687623437942986302690599232729065536417757505209285175593543234585659130582659013242346666628394528555



#n=(a*x+b)*(a*p+b) %m
dec=pow(enc_long, e, n%m)


dec=c.long_to_bytes(dec)
print(dec)