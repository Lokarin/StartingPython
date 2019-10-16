# -*- coding: utf-8 -*-

#############Random##############
import random

def dado(a, b):
	numero = random.randint(a, b)
	print numero

x = 0 

while x < 10:
	dado(1, 6)
	x = x + 1

############Choice###############

lista = [1, 46, 8, 92]
def escolha():
	numero = random.choice(lista)
	print numero

y = 0 

while y < 10:
	escolha()
	y = y + 1


	