#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


alunos=pd.DataFrame({'Nome':['Ary','Cátia','Denis','Beto','Bruna','Dara','Carlos','Alice'],
                    'Sexo':['M','F','M','M','F','F','M','F'],
                    'Idade':[10,20,30,40,50,60,70,80],
                    'Notas':[1,2,3,4,5,6,7,8],
                    'Aprovado':[False,False,False,False,False,False,True,True,]},
                   columns=['Nome','Idade','Sexo','Notas','Aprovado' ])


# In[ ]:


#Crie um DataFrame somente com os alunos aprovados.


# In[10]:


selecao=alunos['Aprovado']==True
aprovados=alunos[selecao]
aprovados


# In[11]:


#Crie um DataFrame somente com as alunas aprovadas.


# In[16]:


selecao = (alunos.Aprovado == True)&(alunos.Sexo == 'F')
aprovadas=alunos[selecao]
aprovadas


# In[17]:


#Crie apenas uma visualização dos alunos com idade entre 10 e 20 anos ou com idade maior ou igual a 40 anos.


# In[18]:


selecao = ((alunos.Idade>10)&(alunos.Idade<20))|(alunos.Idade>=40)
alunos[selecao]


# In[ ]:




