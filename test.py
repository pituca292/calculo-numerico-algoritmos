#!/usr/bin/env
# -*- coding: utf-8 -*-
import math

import matplotlib.pyplot as plt
import numpy as np

import gauss
import solve


def y(x):  # Função y(x)
    return 1/x


def y_2(x):
    return -1/math.pow(x, 2)


def y_3(x):
    return 2/math.pow(x, 3)


def q(x):
    return 1/math.pow(x, 2)  # Função q(x)


def r(x):
    return 1/math.pow(x, 3)  # Função q(x)


# Extremos
a = 1
b = 2
# Solução da equação nos extremos - alfa e beta
a_ = y(a)
b_ = y(b)

# Número de passos (inserido pelo usuário)
n = int(input("Insira o valor máximo de n: "))

e = []
e_max = []

for n in range(5, n+1, 5):
    # print("##### Para n = ", n, "#####")
    # Tamanho total do intervalo
    h = (b - a) / n

    # Malha de pontos
    x = []
    for i in range(1, n):
        x.append(a + i*h)

    # Vetor solução real
    v_sol = solve.solve(y, x, n)
    print("Solução real")
    print(np.matrix(v_sol))

    v_gauss = gauss.v_gauss(q, r, x, h, n, a_, b_)
    # print("Solução Gauss")
    # print(np.matrix(v_gauss))

    # Comparação entre soluções
    dif = abs(np.matrix(v_sol) - np.matrix(v_gauss))
    e.append(dif)
    e_max.append(np.max(dif))
    # print("Diferença entre real e gauss (Erro)")
    # print(dif)
    # print("Erro máximo")
    # print(np.max(dif))

print(e)
plt.semilogy(range(5, n+1, 5), e_max, 'ko')
plt.ylabel('Erro')
plt.xlabel('n')
plt.title('Erro')
# plt.savefig("test.png")
plt.show()
