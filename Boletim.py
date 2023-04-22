#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


##Criando um DataFrame


# In[18]:


boletim=[('Cristiane', 'F', 42, 6, False),
        ('Paula','F',40,10, True),
        ('Lilian','F',44, 9, True)]
boletim=pd.DataFrame(boletim,'1 2 3'.split(),'Nome Genero Idade Nota Aprovada'.split())


# In[19]:


boletim


# In[ ]:


##Exiindo somente os reprovados


# In[20]:


selecao=boletim['Aprovada']==False
reprovados=boletim.loc[selecao,['Nome','Genero', 'Idade']]
reprovados


# In[ ]:


##Exibindo somente os reprovados de outra forma


# In[26]:


selecao=boletim['Aprovada']==False
reprovados=boletim[['Nome', 'Genero', 'Idade']][selecao]
reprovados


# In[ ]:


##Exibindo somente os aprovados


# In[28]:


selecao=boletim['Aprovada']==True
aprovados=boletim[['Nome','Genero', 'Idade']][selecao]
aprovados


# In[ ]:




