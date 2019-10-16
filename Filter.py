# -*- coding: utf-8 -*-

#Filter

def pares(i): #def = Definição
	if i % 2 == 0:
		return i

def impares(i): 
	if i % 2 == 1:
		return i


lista = [1,2,3,4,5,6,7,8,9,10]

listaPares = filter(pares, lista)
				   #func., lista

listaImpares = filter(impares, lista)

print(list(listaPares))	
print(list(listaImpares))

