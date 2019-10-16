# -*- coding: utf-8 -*-

w = open("arquivo2.txt", "a") # w - cria um arquivo novo e no caso dele ja existir, ele apaga tudo. a - ele apenas vai fazer alterações no arquivo

w.write("Bom Dia, esse é o meu arquivo!\n")

w.close()