#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import csv
import psutil

start=time.time()
l1 = []
l2 = []
with open(r'/Users/Mac/Downloads/TranslateWords Challenge/french_dictionary.csv', 'r') as r:
    ref = r.readlines()
for i in ref:
    a = i.split(',')
    l1.append(str(a[0]))
    l2.append(str(a[1].split('\n')[0]))
dict = dict(zip(l1, l2))

with open(r'/Users/Mac/Downloads/TranslateWords Challenge/t8.shakespeare.txt', 'r') as file:
    data = file.read()
    search = ' '.join([dict.get(i, i) for i in data.split()])
for key, value in dict.items():
    search = search.replace(key, value)
print(search)
c={}
for i in dict.keys():
    co=(data.split().count(i))
    c[str(i)]=co
print(c)

with open('/Users/Mac/Desktop/out /frequency.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in c.items():
       writer.writerow([key, value])

with open(r'/Users/Mac/Desktop/out /t8.shakespeares.translated.txt', 'w') as file:
    file.write(search)
end = time.time()
duration = end-start

a = ("Time to process:",(duration), "sec")
b = ('RAM Used (MB):', psutil.virtual_memory()[3]/1000000)
with open(r'/Users/Mac/Desktop/out /performance.txt', 'w') as file:
    file.write(str(a)+"\n"+str(b))

