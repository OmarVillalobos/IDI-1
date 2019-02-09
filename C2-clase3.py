
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


x1 = pd.ExcelFile('C:\\Users\\if686748\\Downloads\\datos.xlsx')
x1.sheet_names[0]


# In[15]:


df = x1.parse(x1.sheet_names[0], header=None)
df


# In[17]:


#x = df.values.sum(axis=1)
x = pd.concat(map(df.get,df.columns)).reset_index(drop=True)
x


# In[ ]:


prom = x.mean()
prom

