#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df1 = pd.DataFrame({'A':{'X':1},'B':{'X':2}})
df2 = pd.DataFrame({'C':{'X':3},'D':{'X':4}})
pd.concat([df1,df2])


# In[9]:


dados=[('A','B'),('C','D')],
df = pd.DataFrame(dados,columns=['L1','L2'], index=['C1','C2'])


# In[10]:


df


# In[11]:


dados = [[1,2,3],[4,5,6]]
index = 'X,Y'.split(',')
columns = list('CBA')[::-1]
df = pd.DataFrame(dados,index,columns)
df


# In[13]:


dados = {'A':{'X':1,'Y':3},'B':{'X':2,'Y':4}}
df = pd.DataFrame(dados)
df


# In[ ]:




