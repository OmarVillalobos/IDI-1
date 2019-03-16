# coding: utf-8

# In[6]:

import pandas as pd 
import random


# In[3]:

data = pd.read_csv('C:/Users/OmarVr/Documents/ITESO/Maestria/IDI/perceptron_simple.csv')


# In[4]:

data


# In[34]:

w_inicial = []
for i in range(5): 
    w_inicial.append(random.random())
w_inicial = pd.Series(w_inicial)


# In[38]:

w_inicial


# In[25]:

features = data.iloc[:,0:5]
features = pd.DataFrame(features)


# In[40]:

feature = features.iloc[0:1,:]
feature = feature.T
feature


# In[43]:

[feature.dot(s)]
