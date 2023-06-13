#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Relatório de Análise VIII - Identificando e Removendo Outliers


# In[6]:


##Importando o pandas, o matplotlib e os dados que serão utilizados


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[10]:


##Atribuindo o arquivo aluguel à variável dados


# In[13]:


dados = pd.read_csv('aluguel.csv', sep = ';')


# In[ ]:


##Criando o box-plot


# In[14]:


dados.boxplot(['Valor'])


# In[ ]:


##Criando uma visualização clara dos dados e realizando uma seleção no DataFrame. Teremos como resultado apenas os dados errôneos


# In[17]:


dados[dados['Valor']>=500000]


# In[18]:


#Gerando algumas estatísticas sobre esses dados. Criando uma series chamada valor.


# In[19]:


valor = dados['Valor']


# In[20]:


##Calculando Q1, o primeiro quartil


# In[22]:


q1 = valor.quantile(.25)
q1


# In[23]:


##Calculando do Q3; em seguida o IIQ, o intervalo interqualítico. Calculando também o limite inferior e superior.


# In[27]:


q1 = valor.quantile(.25)
q3 = valor.quantile(.75)
IIq = q3 - q1
limite_inferior = q1 - 1.5 * IIq
limite_superior = q3 + 1.5 * IIq


# In[ ]:


##Fazendo a seleção dos dados que estão apenas dentro deste dois limites


# In[30]:


selecao = (valor>=limite_inferior)&(valor<=limite_superior)
dados_new = dados [selecao]


# In[31]:


##Gerando novamente o box - plot utilizando a variável dados_new


# In[33]:


dados_new.boxplot(['Valor'])


# In[34]:


##Gerando Histogramas


# In[35]:


dados.hist(['Valor'])
dados_new.hist(['Valor'])


# In[ ]:




