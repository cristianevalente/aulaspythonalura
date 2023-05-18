#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Criando agrupamentos


# In[2]:


##Importando o pandas:


# In[3]:


import pandas as pd


# In[4]:


dados = pd.read_csv('aluguel.csv',sep=';')


# In[5]:


##Visualizando as dez primeiras assinaturas


# In[6]:


dados.head(10)


# In[7]:


##Coletando a variável valor e calculando a média dos valores


# In[8]:


dados['Valor'].mean()


# In[9]:


##Coletando médias segundo alguns tipos de variáveis


# In[10]:


bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo','Flamengo', 'Tijuca']
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]


# In[11]:


##Apenas os dados selecionados estarão em nossa listagem:


# In[12]:


dados['Bairro'].drop_duplicates()


# In[13]:


##Criando os primeiros grupos com base nos dados selecionados. Atribuindo esse conteúdo a variável grupo_bairro


# In[14]:


grupo_bairro = dados.groupby('Bairro')


# In[ ]:


##Verificando o tipo de dados


# In[19]:


type(grupo_bairro)


# In[20]:


##Fazendo um laço para exibir os bairros


# In[21]:


for bairro, dados in grupo_bairro:
    print(bairro)


# In[22]:


##Verificando agora o tipo de dados


# In[23]:


type(grupo_bairro)


# In[24]:


##Extraindo o valor médio com base em nossa lista de bairros


# In[26]:


for bairro, dados in grupo_bairro:
    print('{} ->{}'.format(bairro,dados.Valor.mean()))


# In[27]:


##Coletando a média de valor


# In[28]:


grupo_bairro['Valor'].mean()


# In[29]:


##Passando a variável Valor e Condomínio. Utilizando o método round() para arredondar os valores


# In[31]:


grupo_bairro[['Valor', 'Condominio']].mean().round(2)


# In[ ]:




