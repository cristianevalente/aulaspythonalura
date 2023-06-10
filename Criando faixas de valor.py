#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando o pandas


# In[2]:


import pandas as pd


# In[3]:


##Chamando o arquivo Aluguel
dados = pd.read_csv('aluguel.csv', sep = ';')
dados.head(10)


# In[4]:


##Criando uma lista
#1 e 2
#3 e 4
#5 e 6
#7 e 8
classes = [0,2,4,6,100]


# In[7]:


##Atribuindo os conteúdos as váriáveis quartos e utilizando o método cut para ajudar a categorizar as classes.
quartos = pd.cut(dados.Quartos,classes)
quartos


# In[8]:


##Gerando a primeira visualização da tabela de frequência
pd.value_counts(quartos)


# In[10]:


##Modificando a frequênca com labels
labels = ['1 e 2 quartos', '3 e 4 quartos', '5 e 6 quartos', '7 quartos ou mais']


# In[11]:


##Organizando as informações de maneira mais clara
quartos = pd.cut(dados.Quartos, classes, labels = labels)
pd.value_counts(quartos)


# In[13]:


##Inserindo um método para incluir o valor mais baixo
quartos=pd.cut(dados.Quartos, classes, labels, include_lowest = True)
quartos


# In[ ]:




