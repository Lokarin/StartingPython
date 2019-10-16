# -*- coding: utf-8 -*-

"""
Strings é um tipo de dados em que se armazena coleções de caractéres (texto)

ELas são declaradas com o uso de áspas("")
Ex:
	var1 = 1
	var2 = "1"
Nesse caso a var dois é uma string, e a um, um valor numérico
"""

#Concatenação

a = "Henrique"
b = "Onuki"

concatenar = a + " " + b + "\n"

print concatenar


#Tamanho de uma String

tamanho = len(concatenar)

print tamanho

print a[2] #printando a letra 2 (que seria a 3, pois 0 é contado)

print concatenar[0:8] #printando da letra 0(H) até a letra 5(e

#Métodos

print concatenar.lower() #Printar em minúsculo
print concatenar.upper() #Printar em maiúsculo

concatenar = concatenar.upper()
print concatenar

print concatenar.strip() #Retira caractéres especiais

minha_string = "o rato roeu a roupa do rei de roma"

minha_lista = minha_string.split("r") #Separa uma String em vários objetos, formando assim uma lista / o que é colocado de parâmetro no parenteses gere uma quebra

print minha_lista

busca = minha_string.find("rei") #POsição de algo na String

print busca

print minha_string[busca:] #Printando a partir do ponto "busca"

minha_string = minha_string.replace("o rei", "a rainha") #Altera um valor por outro

print minha_string


