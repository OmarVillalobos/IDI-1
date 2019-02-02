class Grafo:
def __init__(self,entero):
self.entero = entero
self.matriz = [[0]*entero]*entero
self.v = 0
self.matriz_del_profe = ([[0,3,1],[3,0,4],[1,4,0]])
def energia(self):
suma = []
for i in range(0, self.entero-1):
suma.append(self.matriz_del_profe[i][i+1])
v = sum(suma)
return(v)

test = [[0,2,1]]
x = Grafo(3)
y = x.energia()
print(y)
