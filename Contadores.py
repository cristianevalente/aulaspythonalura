#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Contadores


# In[13]:


##Importando o pandas


# In[14]:


import pandas as pd


# In[15]:


##Criando uma Series para abrigar uma lista de caracteres com repetições


# In[16]:


s = pd.Series(list('asdadeadesdaserda'))
s


# In[17]:


##Coletanndo os caracteres disponíveis e eliminando as repetições


# In[18]:


s.unique()


# In[19]:


##Verificando quantas vezes cada um se repetiu


# In[20]:


s.value_counts()


# In[21]:


##Verificando como isto pode ser utilizado em um banco de dados. Importando o banco de dados aluguel


# In[22]:


dados = pd.read_csv('aluguel.csv', sep=';')


# In[23]:


##Descobrindo os tipos de imóveis cadastrados


# In[24]:


dados.Tipo.unique()


# In[25]:


##Podemos utilizar o value_counts()


# In[26]:


dados.Tipo.value_counts()


# In[ ]:




