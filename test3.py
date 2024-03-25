import requests
import time
import os
import threading
import time
import numpy

num_threads = 60
time.time()

def d():
  while len(download_list) > 0:
    d_id = download_list[0]
    download_list.remove(d_id)
    if (d_id in downloaded_list): continue
    downloaded_list.append(d_id)
    print(f'Start to download map with ID {d_id}.')
    resp = requests.get(f'https://beatconnect.io/b/{d_id}')
    with open(f"./map/{d_id}.osz", 'wb') as f:
        for buff in resp:
            f.write(buff)
    print(f'Map with ID {d_id} is downloaded.')
    time.sleep(1)  

def downloadMap():
  if len(download_list) <= 0: return
  
  d_id = download_list[0]
  download_list.remove(d_id)
  if (d_id in downloaded_list): return d_id
  downloaded_list.append(d_id)
  
  resp = requests.get(f'https://beatconnect.io/b/{d_id}')
  with open(f"./map/{d_id}.osz", 'wb') as f:
      for buff in resp:
          f.write(buff)
  print(f'Map with ID {d_id} is downloaded.')
  time.sleep(60)
  return d_id

downloaded_list = [x.split('.')[0] for x in os.listdir('./map')]

id_list = []
with open(f'./songs_id.txt', 'r') as f1:
  id_list = f1.readlines()
id_list = [x[:-1] for x in id_list]

download_list = [x for x in id_list if x not in downloaded_list]

t = [threading.Thread(target=d, name=f't{i+1}') for i in range(num_threads)]
for i in t:
  i.start()
for i in t:
  i.join()



  
