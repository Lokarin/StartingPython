# -*- coding: utf-8 -*-

#List Comprehension 


#---Metodo 1---

#x = [1, 2, 3, 4, 5]
#y = []

#for i in x:
#	y.append(i**2)

#print y

#-----


#---Metodo 2---

x = [1 ,2 ,3, 4, 5]
y = [i**2 for i in x] #Valores ao quadrado
z = [i for i in x if i%2 == 1] #Valores Ímpares


print(y)
print(z)
