
# coding: utf-8

# In[93]:


# notas matrix.iloc[0,0] col then rows
import random
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[88]:


matrix = pd.read_csv('C:\\Users\\if686748\\Documents\\matriz-distancias-5.csv', encoding='ISO-8859-1', header=0)
matrix


# In[89]:


matrix = matrix.set_index('names')


# In[90]:


matrix


# In[136]:


np.sum(matrix,axis= 0)


# In[58]:


t_inicial = 20 
T = []
for i in range(10): 
    t = t_inicial / math.log(2 + i)
    T.append(t)
    print(t)


# In[59]:


plt.plot(T)


# In[129]:


rand1 = random.randrange(len(matrix))
rand2 = random.randrange(len(matrix))
while rand2 == rand1:
    rand2 = random.randrange(len(matrix))


# In[130]:


x = list(range(0,len(matrix)))
x[rand1],x[rand2] = x[rand2],x[rand1]
x


# In[145]:


def distancia(matrix,x):
    distance = []
    for i in range(0,len(matrix)-1):
        distance.append(matrix.iloc[x[i],x[i+1]])
    distance.append(matrix.iloc[x[-1],x[0]])
    distance


# In[146]:


sum(location)


# In[ ]:


for i in range(1,10):
    
    rand1 = random.randrange(len(matrix))
    rand2 = random.randrange(len(matrix))
        while rand2 == rand1:
            rand2 = random.randrange(len(matrix))

