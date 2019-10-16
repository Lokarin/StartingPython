# -*- coding: utf-8 -*-
import math

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

d = b**2-4*a*c 
#discriminante

if d < 0:
    print "Sem Soloção"
elif d == 0:
    x1 = -b / (2*a)
    print "A única Soloção é: ",x1
else: # if d > 0
    x1 = (-b + math.sqrt(d)) / (2*a)  #sqrt - raíz quadrada
    x2 = (-b - math.sqrt(d)) / (2*a)
    print "As soluções são: ",x1,"e",x2