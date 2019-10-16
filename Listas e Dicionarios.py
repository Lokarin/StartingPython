# -*- coding: utf-8 -*-

"""
LISTAs:
	NO geral, um conjunto, seja numérico ou de strings
	Ex:
		var1 = [1, 2, 3, 4]
		var2 = ["henrique", "bernardo", "Guilherme"]
"""

minha_lista = ["abacate", "abacaxi", "melancia"]
minha_lista2 = [1, 2, 3, 4]
minha_lista3 = ["abacaxi", 9.9, 8, True]

print minha_lista
#print minha_lista[2]
"""
for item in minha_lista:
	print item
"""

tamanho = len(minha_lista)
print tamanho

minha_lista.append("laranja") #append - adiciona coisas a lista

if "laranja" in minha_lista:
	print "A laranja está na lista"
else:
	print "A laranja não está na lista"

del minha_lista[2:] #para apagar a lista inteira se deixa apenas o :

print minha_lista

#############################################################

lista = [1 ,33, 2, 4545, 236, 768, 21321, 546, 4, 764]

lista.sort()
#lista = sorted(lista)
#lista.sort(reverse=True) #Decrescente
#lista.reverse() #inverte a lista
#esses comandos funcionam para listas strings, ele toma como regra o alfabeto

print lista

#############################################################
#Dicionários

dicionario_sites = {"google": "google.com", "udemy": "udemy.com"}

#print dicionario_sites["google"]

for chave in dicionario_sites:
	print dicionario_sites[chave]

