# -*- coding: utf-8 -*-

"""
permitem a modularização do código

executaram um bloco quando forem chamadas

Sao definidas pela palavra reservada DEF

def NOME(PARÂMETROS):
	COMANDOS

são chamadas por NOME(ARGUMENTOS)
"""

"""def soma(a, b):
	print a + b

soma(1, 2)"""


def somaReturn(x, y):
	return x + y


def multiplicacao(c, d):
	return c * d


s = somaReturn(1, 2)
m = multiplicacao(2, 2)
print(s)
print(m)

print(somaReturn(s, m))