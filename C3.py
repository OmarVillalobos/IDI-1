
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np


# In[9]:


df = pd.ExcelFile('C:\\Users\\if686748\\Downloads\\datosPE.xlsx')
df.sheet_names


# In[10]:


df = df.parse(df.sheet_names[0], header=0)


# In[11]:


df.head()


# In[13]:


df['imc'] = df['Peso']/df['Estatura']**2


# In[14]:


df.head()


# In[31]:


peso_mean = df['Peso'].mean()


# In[32]:


estatura_mean = df['Estatura'].mean()


# In[30]:


id_mayor_menor = df[df['imc'] == df['imc'].max()]['ID Persona']
id_mayor_menor


# In[23]:


imc_mayor_id = df[df['imc'] >= 30]['ID Persona']


# In[38]:


resultados =[df['imc'],peso_mean,estatura_mean,id_mayor_menor,imc_mayor]


# In[54]:


print(' -----------> tabla IMC \n{0}\n -----------> Promedio de peso es igual a {1}\n ''-----------> Promedio de estatura {2}\n -----------> ID del Mayor peso menor Estatura {3} ''\n -----------> Dataset con IMC mayor a 30 \n{4}'.format(resultados[0],
                                                 resultados[1],
                                                 resultados[2],
                                                 int(resultados[3]),
                                                 resultados[4]))

