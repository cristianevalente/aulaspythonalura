#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Importando o pandas


# In[8]:


import pandas as pd


# In[9]:


#Testando moedas. Verificando se não estão viciadas. Testando cinco moedas.


# In[10]:


m1 = 'CCcCCccCCCccCcCccCcCcCCCcCCcccCCcCcCcCcccCCcCcccCc'
m2 = 'CCCCCccCccCcCCCCccCccccCccCccCCcCccCcCcCCcCccCccCc'
m3 = 'CccCCccCcCCCCCCCCCCcccCccCCCCCCccCCCcccCCCcCCcccCC'
m4 = 'cCCccCCccCCccCCccccCcCcCcCcCcCcCCCCccccCCCcCCcCCCC'
m5 = 'CCCcCcCcCcCCCcCCcCcCCccCcCCcccCccCCcCcCcCcCcccccCc'


# In[11]:


##Montando um DataFrame para tirarmos conclusões


# In[13]:


eventos={'m1':list(m1),
         'm2':list(m2),
         'm3':list(m3),
         'm4':list(m4),
         'm5':list(m5)}
moedas=pd.DataFrame(eventos)
df=pd.DataFrame(data = ['Cara','Coroa'],
               index=['c','C'],
               columns=['Faces'])
for item in moedas:
    df=pd.concat([df,moedas[item].value_counts()], axis = 1)
df


# In[ ]:




