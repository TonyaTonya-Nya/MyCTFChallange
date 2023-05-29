p =9631668579539701602760432524602953084395033948174466686285759025897298205383
gx = 5664314881801362353989790109530444623032842167510027140490832957430741393367
gy = 3735011281298930501441332016708219762942193860515094934964869027614672869355
Ax=3829488417236560785272607696709023677752676859512573328792921651640651429215
Ay=7947434117984861166834877190207950006170738405923358235762824894524937052000
Bx=9587224500151531060103223864145463144550060225196219072827570145340119297428
By=2527809441042103520997737454058469252175392602635610992457770946515371529908

M=Matrix([[Ax,1],[Bx,1]])
w=vector([Ay^2-Ax^3,By^2-Bx^3])
a,b = M.solve_right(w)
a = a % p
b = b % p

print(a,b)

F=GF(p)
a=F(a)
b=F(b)
R.<x>=PolynomialRing(F)
f=x^3+a*x+b
print(f.factor())

alpha=-8778425668366493782038529472271552171423076833119284811370540338595974272969%p
beta=-1706485822346415641443806104662801825943914230110363749830437374602647864828%p
print(alpha,beta)

M=IntegerModRing(p)
alpha=M(alpha)
beta=M(beta)
print(alpha,beta)

phiA=(Ay**2+2*Ay*(alpha-beta).sqrt()*(Ax-alpha)+(alpha-beta)*(Ax-alpha)**2)%p/(Ay**2-(alpha-beta)*(Ax-alpha)**2)%p
phig=(gy**2+2*gy*(alpha-beta).sqrt()*(gx-alpha)+(alpha-beta)*(gx-alpha)**2)%p/(gy**2-(alpha-beta)*(gx-alpha)**2)%p
print(phiA,phig)

d=discrete_log(phiA,Mod(phig,p))
print(d)