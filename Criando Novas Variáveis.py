#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Relatório de Análise VI


# In[2]:


##Criando novas variáveis


# In[ ]:


##Importando o Pandas


# In[3]:


import pandas as pd


# In[6]:


##Coletando o banco de dados


# In[7]:


dados = pd.read_csv('aluguel.csv',sep=';')


# In[ ]:


##Verificando os dez primeiros registros


# In[8]:


dados.head(10)


# In[15]:


dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']


# In[ ]:


##Visualizando a tabela


# In[16]:


dados.head(10)


# In[ ]:


##Criando outra variável que armazenará o valor por metro quadrado (Valor m2). Coletando valor e dividindo por Área


# In[14]:


dados['Valor m2'] = dados['Valor']/ dados['Area']


# In[17]:


##Visualizando a tabela


# In[18]:


dados.head(10)


# In[19]:


##Arredondando os valores


# In[21]:


dados['Valor m2'] = dados['Valor m2'].round(2)


# In[22]:


##Visualizando a tabela


# In[23]:


dados.head(10)


# In[24]:


##Criando uma variável para o valor bruto do metro quadrado(Valor Bruto m2)


# In[25]:


dados['Valor Bruto m2'] = (dados['Valor Bruto']/dados['Area']).round(2)


# In[26]:


##Visualizando a tabela


# In[27]:


dados.head(10)


# In[28]:


##Criando uma variável que abrigue os tipos de imóvel casa e apartamento.
##Para tanto, devemos coletar a variável Tipo, recolher esses marcadores e identifica-los


# In[29]:


casa = ['Casa', 'Casa Condominio', 'Casa de Vila']


# In[31]:


##Criando a variável Tipo Agregado.
##Evocando dados.
##Passando a variável Tipo, seguido pelo método apply()(este método permite que apliquemos uma função a cada registo do DataFrame)


# In[34]:


dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x:'Casa' if x in casa else 'Apartamento')


# In[36]:


##Exibindo a tabela


# In[37]:


dados.head(10)


# In[ ]:




