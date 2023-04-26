#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Relatório de Análise


# In[2]:


##Tratando dados faltantes


# In[3]:


##Importando o Pandas


# In[4]:


import pandas as pd


# In[5]:


##Chamando o arquivo "aluguel"


# In[6]:


dados=pd.read_csv('aluguel.csv', sep=';')


# In[7]:


##Exibindo os primeiros dez elementos


# In[8]:


dados.head(10)


# In[9]:


##Verificando os dados nulos


# In[10]:


dados.isnull()


# In[11]:


##Exibindo informações do DataFrame


# In[12]:


dados.info()


# In[13]:


##Variáveis com dados faltantes


# In[14]:


dados['Valor'].isnull()


# In[15]:


##Coletando os registros diretamente no banco de dados


# In[16]:


dados[dados['Valor'].isnull()]


# In[17]:


##Elilminando os dados nulos


# In[18]:


A=dados.shape[0]
dados.dropna(subset=['Valor'])
B = dados.shape[0]
A-B


# In[19]:


##Trouxe o resultado 0. Será necessário o inplace para trazer 


# In[21]:


A = dados.shape[0]
dados.dropna(subset=['Valor'], inplace=True)
B = dados.shape[0]
A-B


# In[ ]:


##Verificando quantas assinaturas temos em um condomínio


# In[24]:


dados[dados['Condominio'].isnull()].shape[0]


# In[25]:


##Filtrando os dados de acordo com o tipo apartamento


# In[29]:


selecao=(dados['Tipo']=='Apartamento')& (dados['Condominio'].isnull())


# In[30]:


##Eliminando as assinaturas nulas ao invés de coletá-las


# In[32]:


A=dados.shape[0]
dados=dados[~selecao]
B=dados.shape[0]
A-B


# In[33]:


#Verificando quantas assinaturas nulas tem no condomínio agora


# In[34]:


dados[dados['Condominio'].isnull()].shape[0]


# In[35]:


##Mantendo os dados e inserindo o valor 0 onde é nulo


# In[38]:


dados=dados.fillna({'Condominio':0,'IPTU':0})


# In[39]:


##Verificando se o número de nulos será 0


# In[41]:


dados.info()


# In[42]:


##Salvando de forma que o DataFrame seja atualizado com estas modificações (sem incluir o índice)


# In[47]:


dados.to_csv('aluguel.csv', sep = ';', index = False)

