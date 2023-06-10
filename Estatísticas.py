#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


precos = pd.DataFrame([['Feira', 'Cebola', 2.5], 
                        ['Mercado', 'Cebola', 1.99], 
                        ['Supermercado', 'Cebola', 1.69], 
                        ['Feira', 'Tomate', 4], 
                        ['Mercado', 'Tomate', 3.29], 
                        ['Supermercado', 'Tomate', 2.99], 
                        ['Feira', 'Batata', 4.2], 
                        ['Mercado', 'Batata', 3.99], 
                        ['Supermercado', 'Batata', 3.69]], 
                        columns = ['Local', 'Produto', 'Preço'])
precos


# In[10]:


##Aplicando o describe() para gerar um conjunto de estatísticas


# In[12]:


produtos = precos.groupby('Produto', sort = False)
produtos.describe().round(2)


# In[16]:


estatisticas = ['mean', 'std', 'min', 'max']
nomes = {'mean': 'Média', 'std': 'Desvio Padrão', 'min': 'Mínimo', 'max': 'Máximo'}
produtos ['Preço'].aggregate(estatisticas).rename(columns = nomes).round(2)


# In[ ]:




