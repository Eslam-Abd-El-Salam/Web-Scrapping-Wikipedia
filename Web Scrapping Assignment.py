#!/usr/bin/env python
# coding: utf-8

# # Assignment

# In[1]:


link = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
#     Year	Physics	Chemistry	Physiologyor Medicine	Literature	Peace	Economics


# ![image.png](attachment:image.png)
# 

# In[4]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    link = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
    res = requests.get(link,timeout=10)
    if res.status_code == 200:  
        soup = BeautifulSoup(res.text,"lxml")
        found_element = soup.find("div",attrs= {"class":"mw-content-ltr mw-parser-output"}).find("tbody").find_all("tr")
        number_of_rows = len(found_element) 
        
        with open("wekibdeda_table.csv", mode="w",encoding="utf-8") as f:
            for i in range(0,number_of_rows):
                data = found_element[i].text.strip().replace("\n\n",",")
                f.write(data)
                f.write("\n")
                #print(data)
            print("Done")
    else:
        print(f"status code {res.status_code}")
        
except requests.exceptions.Timeout:
    print("Timed out")
    
except:
    print("Invalid Link")

df = pd.read_csv("wekibdeda_table.csv")
df.head()


# In[ ]:





# In[ ]:




