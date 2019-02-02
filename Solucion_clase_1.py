# coding: utf-8

# In[1]:


class graf(object):
    def __init__(self,matriz: list, longitud: int):
        self.matriz = matriz
        self.longitud = longitud
        self.valor = 0
        
    def energia(self, comb: list):
        self.valor = 0 
        for i,d in enumerate(comb):
            if (i < self.longitud -1)
            self.valor += self.matriz[d][comb[i+1]]
        else: 
            self.valor += self.matriz[d][0]


# In[5]:


enumerate([1,2,3])


# In[7]:


from grafo import graf

def main():
    nig = graf([[0,3,1],[3,0,4],[1,4,0]],3)
    
    nig = energia([0,2,1])
    print(str(nig.valor))
if __name__ == '__main__':
    main()

