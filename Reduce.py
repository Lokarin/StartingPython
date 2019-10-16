# -*- coding: utf-8 -*-

#Reduce
from functools import reduce

def soma(x, y):
	return x + y

lista = [1 ,6, 76, 3, 59, 90]

soma = reduce(soma, lista)

print(soma)
