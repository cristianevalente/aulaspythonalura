#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Relatório de Análise IV
##Seleção e Frequências


# In[18]:


import pandas as pd


# In[19]:


dados = pd.read_csv('dados/aluguel.csv', sep = ';')


# In[20]:


dados.head(10)


# In[21]:


# Selecione somente os imóveis classificados com tipo 'Apartamento'.


# In[22]:


selecao=dados['Tipo']=='Apartamento'
selecao


# In[23]:


selecao=dados['Tipo']=='Apartamento'
n1=dados[selecao].shape[0]
n1


# In[24]:


# Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.


# In[25]:


selecao=(dados['Tipo']=='Casa')|(dados['Tipo']=='Casa de Condomínio')|(dados['Tipo']=='Casa da Vila')
n2=dados[selecao].shape[0]
n2


# In[26]:


# Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.


# In[27]:


selecao=(dados['Area'] >= 60) & (dados['Area'] <= 100)
n3=dados[selecao].shape[0]
n3
                            


# In[28]:


# Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.


# In[29]:


selecao=(dados['Quartos']>=4)&(dados['Valor']<2000)
n4=dados[selecao].shape[0]
n4


# In[31]:


print("Nº de imóveis classificados com o tipo 'Apartamento'->{}".format(n1))


# In[32]:


print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'->{}".format(n3))


# In[33]:


print ("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites->{}".format(n3))


# In[34]:


print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00->{}".format(n4))


# In[ ]:




