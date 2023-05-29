import requests
from requests import get


set="9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"

for i in range(80000,89999):

    string="http://ir.lib.ntust.edu.tw/bitstream/987654321/"+str(i)+"/1"
    web = requests.get(string)  
    if("html" in web.text):
        continue
    else:
        print(i)

