#!/usr/bin/env python
# coding: utf-8

# In[51]:


#Relatório de Análise II


# In[52]:


##Tipos de Dados


# In[53]:


import pandas as pd


# In[54]:


dados=pd.read_csv('dados/aluguel.csv',sep=';')


# In[55]:


dados.head(10)


# In[56]:


dados['Tipo']


# In[57]:


dados.Tipo


# In[58]:


tipo_de_imovel=dados['Tipo']


# In[59]:


type(tipo_de_imovel)


# In[60]:


tipo_de_imovel.drop_duplicates()


# In[61]:


tipo_de_imovel.drop_duplicates(inplace=True)


# In[62]:


tipo_de_imovel


# In[63]:


##Organizando a visualização


# In[64]:


tipo_de_imovel=pd.DataFrame(tipo_de_imovel)


# In[65]:


tipo_de_imovel


# In[66]:


tipo_de_imovel.index


# In[67]:


tipo_de_imovel.shape[0]


# In[68]:


range(tipo_de_imovel.shape[0])


# In[69]:


for i in range(tipo_de_imovel.shape[0]):
    print(i)


# In[70]:


tipo_de_imovel.index=range(tipo_de_imovel.shape[0])


# In[71]:


tipo_de_imovel


# In[72]:


tipo_de_imovel.columns.name='id'
tipo_de_imovel


# In[73]:


import pandas as pd


# In[74]:


data=[1,2,3,4,5]
s=pd.Series(data)


# In[75]:


s


# In[76]:


index=['Linha'+str(i)for i in range (5)]


# In[77]:


index


# In[78]:


s=pd.Series(data=data, index=index)


# In[79]:


s


# In[80]:


data={'Linha'+str(i):i+1 for i in range (5)}


# In[81]:


data


# In[82]:


s=pd.Series(data)


# In[83]:


s


# In[84]:


s1=s+2


# In[85]:


s1


# In[ ]:




