#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd


# In[49]:


data=[1,2,3,4,5]


# In[50]:


s=pd.Series(data)


# In[51]:


s


# In[52]:


index=['Linha'+str(i)for i in range(5)]


# In[53]:


index


# In[54]:


s = pd.Series(data = data, index = index)


# In[55]:


s


# In[56]:


data={'Linha' + str (i) : i + 1 for i in range (5)}


# In[57]:


data


# In[58]:


s = pd.Series (data)


# In[59]:


s


# In[60]:


s1 = s + 2


# In[61]:


s1


# In[62]:


s2 = s1 - 2


# In[63]:


s2


# In[64]:


data = [[1,2,3],
       [4,5,6],
       [7,8,9]]


# In[65]:


df1 = pd.DataFrame(data = data)


# In[66]:


df1


# In[67]:


index = ['Linha' + str(i) for i in range(3)]


# In[68]:


index


# In[69]:


df1 = pd.DataFrame(data = data, index = index)


# In[70]:


df1


# In[71]:


columns = ['Coluna' + str (i) for i in range(3)]


# In[72]:


columns


# In[73]:


df2 = pd.DataFrame(data = data, index = index, columns = columns)


# In[74]:


df2


# In[75]:


data = {'Coluna 0':{'Linha0':1,  'Linha1':4,  'Linha 2':7},
        'Coluna 1':{'Linha0':2,  'Linha1':5,  'Linha 2':8},
        'Coluna 2':{'Linha0':3,  'Linha1':6,  'Linha 2':9}}


# In[76]:


data


# In[77]:


data = [(1,2,3),
        (4,5,6),
       (7,8,9)]


# In[78]:


data


# In[79]:


df3 = pd.DataFrame(data = data, index = index, columns = columns)


# In[80]:


df3


# In[81]:


df1[df1 > 0] = 'A'
df1


# In[82]:


df2[df2 > 0] = 'B'
df2


# In[83]:


df3[df3 > 0] = 'C'
df3


# In[84]:


df4 = pd.concat([df1, df2, df3])
df4


# In[85]:


df4 = pd.concat([df1, df2, df3], axis = 1)
df4


# In[ ]:




