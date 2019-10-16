# -*- coding: utf-8 -*-

#Função Enumerate

lista = ["abacate", "bola", "cachorro"]

#---Método 1---

#for i in range(len(lista)):
#	print (i, lista[i])

#-----


#---Método 2---

for i, nome in enumerate(lista):
	print(i, nome)