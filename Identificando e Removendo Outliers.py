#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Relatório de Análise VIII - Identificando e Removendo Outliers


# In[2]:


##Importando o pandas, o matplotlib e os dados que serão utilizados


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[4]:


##Atribuindo o arquivo aluguel à variável dados


# In[5]:


dados = pd.read_csv('aluguel.csv', sep = ';')


# In[6]:


##Criando o box-plot


# In[7]:


dados.boxplot(['Valor'])


# In[8]:


##Criando uma visualização clara dos dados e realizando uma seleção no DataFrame. Teremos como resultado apenas os dados errôneos


# In[9]:


dados[dados['Valor']>=500000]


# In[10]:


#Gerando algumas estatísticas sobre esses dados. Criando uma series chamada valor.


# In[11]:


valor = dados['Valor']


# In[12]:


##Calculando Q1, o primeiro quartil


# In[13]:


q1 = valor.quantile(.25)
q1


# In[14]:


##Calculando do Q3; em seguida o IIQ, o intervalo interqualítico. Calculando também o limite inferior e superior.


# In[15]:


q1 = valor.quantile(.25)
q3 = valor.quantile(.75)
IIq = q3 - q1
limite_inferior = q1 - 1.5 * IIq
limite_superior = q3 + 1.5 * IIq


# In[16]:


##Fazendo a seleção dos dados que estão apenas dentro deste dois limites


# In[17]:


selecao = (valor>=limite_inferior)&(valor<=limite_superior)
dados_new = dados [selecao]


# In[18]:


##Gerando novamente o box - plot utilizando a variável dados_new


# In[19]:


dados_new.boxplot(['Valor'])


# In[20]:


##Gerando Histogramas


# In[21]:


dados.hist(['Valor'])
dados_new.hist(['Valor'])


# In[ ]:


##Criando o box-plot


# In[22]:


dados.boxplot(['Valor'], by = ['Tipo'])


# In[23]:


##Fazendo análise para os grupos selecionados


# In[24]:


grupo_tipo = dados.groupby('Tipo')


# In[25]:


##Criando grupos baseados na variável Valor por Tipo. Mudando o tipo de DataFrameGroup para Series


# In[26]:


grupo_tipo = dados.groupby('Tipo')['Valor']


# In[27]:


##Visualizando o conteúdo dos dados


# In[28]:


grupo_tipo.groups


# In[29]:


##Criando estatísticas


# In[30]:


Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1-1.5*IIQ
limite_superior = Q3+1.5*IIQ


# In[31]:


##Acessando limite_superior de um tipo de imóvel do tipo apartamento


# In[32]:


limite_superior['Apartamento']


# In[33]:


##identificando dados discrepantes de acordo com os tipos de apartamento


# In[35]:


for tipo in grupo_tipo.groups.keys():
    print(tipo)


# In[36]:


##Realizando uma seleção com mais de um tipo de variável(Tipo e Valor)


# In[40]:


for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor']>=limite_inferior[tipo])&(dados['Valor']<=limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados[selecao]


# In[41]:


##Criando um DataFrame com essa seleção que criamos


# In[44]:


dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor']<=limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])


# In[ ]:


##Exibindo o DataFrame


# In[45]:


dados_new


# In[ ]:


##Gerando um novo box-plot utilizando dados_new


# In[49]:


dados_new.boxplot(['Valor'],by = ['Tipo'])


# In[50]:


##Salvando os dados para utilizá-los em análises posteriores


# In[52]:


dados_new.to_csv('aluguel_residencial_sem_outliers.csv',sep=';', index = False)


# In[ ]:




