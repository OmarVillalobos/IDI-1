
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import random
from math import e 


# In[44]:


# data = pd.read_csv('C:/Users/OmarVr/Documents/ITESO/Maestria/IDI/perceptron_simple.csv')
# data = pd.read_csv('C:/Users/if686748/Documents/perceptron_simple.csv')
#data = pd.ExcelFile('/Users/omar/Documents/Python/Maestria/IDI/tabla_para_probar.xlsx')
data = pd.ExcelFile('C:/Users/if686748/Downloads/tabla_para_probar.xlsx')
data = data.parse(data.sheet_names[0], header=0)
x = data.iloc[:,:-2]
d = data.iloc[:,-2:]
x


# In[45]:


N = len(x.iloc[0]) # Numero de entradas/ variables/columnas
M = 2 #numero de salidas / variables dependientes
Q = len(data) # Filas / Learning patterns 
L = N*M  # recomendacion N * M 
print(N,M,Q,L)


# In[123]:


matriz_Wh = np.random.random((L, N))
matriz_Wo = np.random.random((L, M))
matriz_Wh
matriz_Wo


# In[129]:


net_h = [None] * L
net_o = list()
y_k = [None] * M
sumatoria_h = []
sumatoria_o = []
y_h = [None] * L 
alpha = 0.1
sumatoria_deltas = []
error = 1.1


# In[130]:


while error > 1e-10 : 
    for p in range(0,Q):
        delta_o = []
        delta_h = []
        net_h = [None] * L
        net_o = list()
        for j in range(0,L):
            sumatoria_h = 0
            for i in range(0,N):
                sumatoria_h += x.iloc[p][i]*matriz_Wh[j][i]
                #sumatoria_h.append(x.iloc[p][i]*matriz_Wh[j][i])
            net_h[j] = sumatoria_h
            y_h[j] = 1/(1+e**(-net_h[j])) 
        for k in range(0,M):
            sumatoria_o = []
            for j in range(0,L):
                sumatoria_o.append(y_h[j]*matriz_Wo[j][k])
            net_o.append(sum(sumatoria_o))
            y_k[k] = 1/(1+e**(-net_o[k]))
            delta_o.append((d.iloc[p][k] - y_k[k])*y_k[k]*(1-y_k[k]))
        for j in range(0,L):
            sumatoria_deltas = []
            for k in range(0,M):
                sumatoria_deltas.append(delta_o[k]*matriz_Wo[j][k])
                matriz_Wo[j][k] += alpha*(delta_o[k]*y_h[j])
            delta_h.append(y_h[j]*(1-y_h[j])*sum(sumatoria_deltas))

        for j in range(0,L):
            for i in range(0,N):
                matriz_Wh[j][i] += alpha*(delta_h[j]*x.iloc[p][i])
    error = (1/2)*sum(delta_o)**2


# In[127]:


error


# In[100]:


net_h

