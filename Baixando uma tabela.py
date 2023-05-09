#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Instalando as bibliotecas Requests e Beautiful Soup


# In[10]:


get_ipython().system('pip install requests')
from bs4 import BeautifulSoup
import pandas as pd


# In[6]:


get_ipython().system('pip install bs4')


# In[16]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.federalreserve.gov/releases/h3/current/default.htm'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
table = soup.findAll('table')
html_file = f'<html><body>{table}</body></html>'
df = pd.read_html(html_file)


# In[17]:


##Acessando o índice para escolher a tabela desejada


# In[18]:


df[0]


# In[ ]:




