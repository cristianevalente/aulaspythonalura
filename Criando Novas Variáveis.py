#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Relatório de Análise VI


# In[3]:


##Criando novas variáveis


# In[4]:


##Importando o Pandas


# In[5]:


import pandas as pd


# In[6]:


##Coletando o banco de dados


# In[7]:


dados = pd.read_csv('aluguel.csv',sep=';')


# In[8]:


##Verificando os dez primeiros registros


# In[9]:


dados.head(10)


# In[10]:


dados['Valor Bruto'] = dados['Valor'] + dados['Condominio'] + dados['IPTU']


# In[11]:


##Visualizando a tabela


# In[12]:


dados.head(10)


# In[13]:


##Criando outra variável que armazenará o valor por metro quadrado (Valor m2). Coletando valor e dividindo por Área


# In[14]:


dados['Valor m2'] = dados['Valor']/ dados['Area']


# In[15]:


##Visualizando a tabela


# In[16]:


dados.head(10)


# In[17]:


##Arredondando os valores


# In[18]:


dados['Valor m2'] = dados['Valor m2'].round(2)


# In[19]:


##Visualizando a tabela


# In[20]:


dados.head(10)


# In[21]:


##Criando uma variável para o valor bruto do metro quadrado(Valor Bruto m2)


# In[22]:


dados['Valor Bruto m2'] = (dados['Valor Bruto']/dados['Area']).round(2)


# In[23]:


##Visualizando a tabela


# In[24]:


dados.head(10)


# In[25]:


##Criando uma variável que abrigue os tipos de imóvel casa e apartamento.
##Para tanto, devemos coletar a variável Tipo, recolher esses marcadores e identifica-los


# In[26]:


casa = ['Casa', 'Casa Condominio', 'Casa de Vila']


# In[27]:


##Criando a variável Tipo Agregado.
##Evocando dados.
##Passando a variável Tipo, seguido pelo método apply()(este método permite que apliquemos uma função a cada registo do DataFrame)


# In[28]:


dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x:'Casa' if x in casa else 'Apartamento')


# In[29]:


##Exibindo a tabela


# In[30]:


dados.head(10)


# In[31]:


##Excluindo variáveis


# In[32]:


dados_aux = pd.DataFrame(dados[['Tipo Agregado','Valor m2', 'Valor Bruto','Valor Bruto m2']])


# In[33]:


##Verificando o DataFrame


# In[34]:


dados_aux.head(10)


# In[35]:


##Excluindo uma variável


# In[36]:


del dados_aux['Valor Bruto']


# In[37]:


##Visualizando a tabela


# In[38]:


dados_aux.head(10)


# In[39]:


##Excluindo através do método pop


# In[40]:


dados_aux.pop('Valor Bruto m2')


# In[41]:


##Verificando do DataFrame


# In[42]:


dados_aux.head(10)


# In[43]:


##Excluindo múltiplas variáveis com o método drop()


# In[46]:


dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True)


# In[47]:


##Verificando o DataFrame


# In[48]:


dados_aux.head(10)


# In[49]:


##Sobrescrevendo o arquivo do Banco de Dados


# In[50]:


dados.to_csv('aluguel.csv', sep=';', index = False)


# In[ ]:




