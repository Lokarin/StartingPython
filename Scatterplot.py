# -*- coding: utf-8 -*-
# Gráfico de Linhas

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
titulo = "Scatterplot: Gráfico de pontos "
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Legendas
#plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.scatter (x, y, label = "Meus Pontos", color = 'r')
plt.plot(x, y)
plt.legend()

plt.show()


