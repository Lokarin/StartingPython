# -*- coding: utf-8 -*-

lista = [3, 2, 1]

for i in range(len(lista)):
	menor = i 

	for j in range(i + 1, len(lista)):
		if lista[j] < lista[menor]:
			menor = j

	if lista[1] != lista[menor]:
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux

print lista

	