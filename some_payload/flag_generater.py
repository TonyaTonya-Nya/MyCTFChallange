'''
將字元分解成兩個數字的 XOR
'''
import random
import sys

input=sys.argv[1]
rand = random.sample(range(1, 127), input.__len__())

encrypt=[]
decrypt=[]

for i in range(0,input.__len__()):
    encrypt.append(ord(input[i])^rand[i])
   
for i in range(0,input.__len__()):
    decrypt.append(chr(encrypt[i]^rand[i]))

print(rand)
print(encrypt)
print(decrypt)