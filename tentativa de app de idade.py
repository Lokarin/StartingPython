# -*- coding: utf-8 -*-

idade = input("Digite sua Idade: ")

if idade >= 18:
	print ("Maior de Idade")
elif idade > 0 and idade < 18:
	print ("Menor de Idade")
else:
	print ("Valor Inválido")