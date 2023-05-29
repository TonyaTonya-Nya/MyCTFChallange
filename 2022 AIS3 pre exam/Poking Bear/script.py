import requests
from requests import get


set="9876543210zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"



for i in range(0,pow(62,5)):

    string="http://hitcup-bugslife.duckdns.org:9491/node/"+str(i)
    web = requests.get(string) 

    print(web.text)
    if("Page not found" in web.text):
        continue
    else:
        print(i)

