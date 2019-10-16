# -*- coding: utf-8 -*-

"""
Eles vao repetir um bloco inteiro enquanto sua condicao for atendida
"""

x = 1

while x < 10:
	print x
	x += 1  # x = x + 1

"""
FOR:
	Para cada valor dentro de uma lista ele executa um bloco
"""

lista = [1, 2, 3, 4, 5]
lista2 = ["Henrique", "Bernardo", "Lucas"]

for i in lista2: # i = elemento da lista
	print(i)

for i in range(10, 20, 2):
	print i