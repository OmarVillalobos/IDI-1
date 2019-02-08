# -*- coding: utf-8 -*-
"""
Editor de Spyder
Este es un archivo temporal
"""
#1. Desarrollar código en Python (no es necesario que sea una clase) que a partir de un entero n>1 genere 
#una lista de n números aleatorios e imprima la suma de los elementos, el mayor y el menor de ellos.
#
#2. Desarrollar una función en Python (no es necesario que sea una clase) que reciba un entero n y 
#determine si es primo o no. Usando la función genere código que imprima los primos 20 números primos.
import random
#class Suma(object):
#   def  __init__(self, entero: int):
#        self.entero = entero
    
#    def suma_mayor_menor(self):
        
    
def suma_mayor_menor(entero: int):
    lista = []
    for i in range(entero):
        lista.append(random.randint(0,1000))
    suma = sum(lista)
    minimo = min(lista)
    maximo = max(lista)
    return(lista,suma,minimo,maximo)

def numero_primo(entero: int):
    if entero == 1:
        return(0)
    for i in range(2,entero):
        if entero % i == 0:
            return(0)
    return(entero)
x = suma_mayor_menor(15) 
print(x)    
x = numero_primo(15)
print(x)

def numeros_primos_20():
    lista = []
    entero = 1
    while len(lista) < 20:
        if numero_primo(entero) != 0:
            lista.append(entero)
        entero += 1
    return(lista)
    
x = numeros_primos_20()
print(x)
