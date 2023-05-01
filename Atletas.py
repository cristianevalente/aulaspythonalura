#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Templo dos atletas


# In[ ]:


Importando o pandas


# In[11]:


import pandas as pd


# In[10]:


##DataFrame com o tempo dos atletas


# In[14]:


atletas = pd.DataFrame([['Marcos', 9.62], ['Pedro', None], ['João', 9.69], 
          ['Beto', 9.72], ['Sandro', None], ['Denis', 9.69], 
          ['Ary', None], ['Carlos', 9.74]], 
          columns = ['Corredor', 'Melhor Tempo'])
atletas


# In[ ]:


##Atribuindo o valor médio de todos os atletas aos dados faltantes


# In[15]:


atletas.fillna(atletas["Melhor Tempo"].mean(),inplace = True)


# In[16]:


atletas


# In[ ]:




