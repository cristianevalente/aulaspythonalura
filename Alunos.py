#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#Novo Boletim


# In[ ]:


#Criando um novo DataFrame


# In[7]:


alunos = pd.DataFrame({'Nome':['Ary', 'Cátia', 'Dênis', 'Beto', 'Bruna', 'Dara', 'Carlos', 'Alice'],
                      'Sexo': ['M','F','M','M','F','F','M','F'],
                      'Idade': [15,27,56,32,42,21,19,35],
                      'Notas': [7.5,2.5,5.0,10,8.2,7,6,5.6]},
                     columns = ['Nome', 'Idade', 'Sexo', 'Notas'])


# In[8]:


##Exibindo os dados do DataFrame


# In[9]:


alunos


# In[11]:


##Criando uma variável que indica a diferença entre cada nota e a média


# In[18]:


alunos['Notas-Média(Notas)'] = alunos['Notas']    .apply(lambda x: x - alunos['Notas'].mean())


# In[ ]:


##Exibindo o DataFrame


# In[17]:


alunos


# In[19]:


##Criando uma variávael indicando faixas etárias para os alunos


# In[21]:


alunos['Faixa Etária'] = alunos['Idade']    .apply(lambda x: 'Menor que 20 anos' if x<20
          else ('Entre 20 a 40 anos' if (x >= 20 and x<=40)
               else 'Maior que 40 anos'))


# In[22]:


##Exibindo o DataFrame


# In[23]:


alunos


# In[24]:


##Criando outra variável que indica a diferença entre cada nota e a média


# In[28]:


alunos['Notas-Média(Notas)'] =     alunos.Notas - alunos.Notas.mean()


# In[29]:


##Exibindo o DataFrame


# In[30]:


alunos


# In[ ]:




