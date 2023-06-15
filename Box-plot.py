#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Criando um boxplot


# In[1]:


import pandas as pd


# In[ ]:


##Atribuindo o arquivo csv a uma variável


# In[4]:


aluguel_amostra = pd.read_csv('aluguel_amostra.csv', sep=';')
aluguel_amostra


# In[ ]:


##Obtendo resultados com describe()


# In[6]:


aluguel_amostra['Valor m2'].describe().round(2)


# In[ ]:


Importando bibliotecas necessárias


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[7]:


aluguel_amostra.boxplot(['Valor m2'])


# In[ ]:




