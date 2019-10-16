# -*- coding: utf-8 -*-

"""
IF:
	Realiza testes condicionais
	executa um bloco SE uma determinada condicao for atendida
	Avalia se a condicao e verdadeira ou nao
"""

a = 5
b = 6 

if a > b:
	print "A variável a é a maior"
if a < b:
	print "A variável b é a maior"


"""
ELSE:
	ele executa um bloco no caso do IF nao ter executado o dele
"""

x = 1
y = 2

if x > y:
	print "x maior que y"
else:
	print "y maior que x"


"""
ELIF:
	caso haja necessidade de mais condiçoes entre if e else
"""

c = 1
d = 2

if c == d:
	print "números iguais"
elif c < d:
	print "c menor que d" #se executa a primeira condição verdadeira que encontrar
elif d > c:
	print "d maior que c" #else não será executado, pois em ordem de prioridade, o else só ocorrem quando nenhum dos if ou elif são executados
else:
	print "números diferentes"