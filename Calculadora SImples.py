# -*- coding: utf-8 -*-
import math

valor1 = float(input("Insira seu primeiro Valor: "))
operacao = raw_input("Insira o operador( +, -, /, *, **, resto):")
valor2 = float(input("Insira seu segundo Valor: "))

#Soma
if operacao == "+":
	soma = valor1 + valor2
	print("Resultado: %f"%soma)

#Subtração
elif operacao == "-":
	subtracao = valor1 - valor2
	print("Resultado: %f"%subtracao)

#Divisão
elif operacao == "/":
	divisao = valor1 / valor2
	print("Resultado: %f"%divisao)

#Multiplicação
elif operacao == "*":
	multiplicacao = valor1 * valor2
	print("Resultado: %f"%multiplicacao)

#Exponenciação
elif operacao == "**":
	elevado = valor1 ** valor2
	print("Resultado: %f"%elevado)

#Resto
elif operacao == "resto":
	resto = valor1 % valor2
	print("Resultado: %f"%resto)

#Erro
else:
	print("Operação Inválida")

