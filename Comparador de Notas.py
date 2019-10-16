# -*- coding: utf-8 -*-

nota1 = float(input("Digite aqui sua primeira nota: "))
nota2 = float(input("Digite aqui sua segunda nota: "))

"""
total = nota1 + nota2
media = total / 2
"""
#print total
#print media

media = (nota1 + nota2)/2

print "Sua média é %f" %(media)

if media >= 6:
	print "Passou"
else:
	print "Reprovou"
