from sympy import Symbol, Poly

#state = int.from_bytes(os.urandom(8), 'little') # 亂數
poly = 0b1010101000001101001110100110011101111110000110111110000010111111
state= 0b1100110111001110101101111000101001001001000101111111100111111100

F.<x>=PolynomialRing(GF(2))
P=x^64+x^63+x^62+x^61+x^60+x^59+x^58+x^56+x^50+x^49+x^48+x^47+x^46+x^44+x^43+x^38+x^37+x^36+x^35+x^34+x^33+x^31+x^30+x^29+x^26+x^25+x^22+x^20+x^19+x^18+x^15+x^13+x^12+x^6+x^4+x^2+1


#P=x^4+x^2+x^1+1
C=companion_matrix(P,format='bottom')
C_a=companion_matrix(P,format='bottom')

for i in range(0,64):
    C_a[i]=(C^(42+43*i))[0]

#求解Ax=b
b=vector([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0])#帶入前四輸出
A=C_a^-1
x=C_a^-1*b

arr=[]
for i in range(64,164):
    arr.append((C^(42+43*i)*x)[0])

print(arr)

