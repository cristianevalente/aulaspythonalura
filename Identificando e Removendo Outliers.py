#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Relatório de Análise VIII - Identificando e Removendo Outliers


# In[3]:


##Importando o pandas, o matplotlib e os dados que serão utilizados


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[5]:


##Atribuindo o arquivo aluguel à variável dados


# In[6]:


dados = pd.read_csv('aluguel.csv', sep = ';')


# In[7]:


##Criando o box-plot


# In[8]:


dados.boxplot(['Valor'])


# In[9]:


##Criando uma visualização clara dos dados e realizando uma seleção no DataFrame. Teremos como resultado apenas os dados errôneos


# In[10]:


dados[dados['Valor']>=500000]


# In[11]:


#Gerando algumas estatísticas sobre esses dados. Criando uma series chamada valor.


# In[12]:


valor = dados['Valor']


# In[13]:


##Calculando Q1, o primeiro quartil


# In[14]:


q1 = valor.quantile(.25)
q1


# In[15]:


##Calculando do Q3; em seguida o IIQ, o intervalo interqualítico. Calculando também o limite inferior e superior.


# In[16]:


q1 = valor.quantile(.25)
q3 = valor.quantile(.75)
IIq = q3 - q1
limite_inferior = q1 - 1.5 * IIq
limite_superior = q3 + 1.5 * IIq


# In[17]:


##Fazendo a seleção dos dados que estão apenas dentro deste dois limites


# In[18]:


selecao = (valor>=limite_inferior)&(valor<=limite_superior)
dados_new = dados [selecao]


# In[19]:


##Gerando novamente o box - plot utilizando a variável dados_new


# In[20]:


dados_new.boxplot(['Valor'])


# In[21]:


##Gerando Histogramas


# In[22]:


dados.hist(['Valor'])
dados_new.hist(['Valor'])


# In[23]:


##Criando o box-plot


# In[24]:


dados.boxplot(['Valor'], by = ['Tipo'])


# In[25]:


##Fazendo análise para os grupos selecionados


# In[26]:


grupo_tipo = dados.groupby('Tipo')


# In[27]:


##Criando grupos baseados na variável Valor por Tipo. Mudando o tipo de DataFrameGroup para Series


# In[28]:


grupo_tipo = dados.groupby('Tipo')['Valor']


# In[29]:


##Visualizando o conteúdo dos dados


# In[30]:


grupo_tipo.groups


# In[31]:


##Criando estatísticas


# In[32]:


Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1-1.5*IIQ
limite_superior = Q3+1.5*IIQ


# In[33]:


##Acessando limite_superior de um tipo de imóvel do tipo apartamento


# In[34]:


limite_superior['Apartamento']


# In[35]:


##identificando dados discrepantes de acordo com os tipos de apartamento


# In[36]:


for tipo in grupo_tipo.groups.keys():
    print(tipo)


# In[37]:


##Realizando uma seleção com mais de um tipo de variável(Tipo e Valor)


# In[38]:


for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor']>=limite_inferior[tipo])&(dados['Valor']<=limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados[selecao]


# In[39]:


##Criando um DataFrame com essa seleção que criamos


# In[40]:


dados_new = pd.DataFrame()
for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    eh_dentro_limite = (dados['Valor']<=limite_superior[tipo])
    selecao = eh_tipo & eh_dentro_limite
    dados_selecao = dados[selecao]
    dados_new = pd.concat([dados_new, dados_selecao])


# In[41]:


##Exibindo o DataFrame


# In[42]:


dados_new


# In[43]:


##Gerando um novo box-plot utilizando dados_new


# In[44]:


dados_new.boxplot(['Valor'],by = ['Tipo'])


# In[45]:


##Salvando os dados para utilizá-los em análises posteriores


# In[46]:


dados_new.to_csv('aluguel_residencial_sem_outliers.csv',sep=';', index = False)


# In[52]:


dados = pd.read_csv('aluguel_amostra.csv', sep = ';')


# In[50]:


area = plt.figure()
g1 = area.add_subplot(1, 2, 1)
g2 = area.add_subplot(1, 2, 2)
grupo1 = dados.groupby('Tipo Agregado')['Valor']
label = grupo1.count().index
valores = grupo1.count().values
g1.pie(valores, labels = label, autopct='%1.1f%%')
g1.set_title('Total de Imóveis por Tipo Agregado')
grupo2 = dados.groupby('Tipo')['Valor']
label = grupo2.count().index
valores = grupo2.count().values
g2.pie(valores, labels = label, autopct='%1.1f%%', explode = (.1, .1, .1, .1, .1))
g2.set_title('Total de Imóveis por Tipo')


# In[ ]:




