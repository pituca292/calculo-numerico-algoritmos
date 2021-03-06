#!/usr/bin/env
# -*- coding: utf-8 -*-
# Módulo de Gauss:
# Métodos de calculo da solução de um sistema linear por eliminação de gauss
# Método para calculo do erro da solução de gauss em relação a solução real

import numpy as np

import construtor
import solve


# Calcula o vetor solução pelo método de Gauss.
# Entradas: matriz, vetor de termos independentes, número de pontos
# Retorno: vetor solução
def v_sol(m, v, n):
    # Verifica e escalona a matriz
    for j in range(n):
        if m[j][j] == 0:
            k = j
            while True:
                if 0 == m[k][j]:
                    k += 1
                    if k == n:
                        print("Matriz inválida")
                        break
                else:
                    temp = m[k].copy()
                    m[k] = m[j].copy()
                    m[j] = temp.copy()
                    break
        for i in range(j + 1, n):
            mult = - m[i][j] / m[j][j]
            for k in range(j, n):
                m[i][k] += mult * m[j][k]
            v[i] += mult * v[j]

    # Resolve a matriz escalonada
    x = [None] * n
    for i in range(n-1, -1, -1):
        x[i] = v[i]
        for j in range(i + 1, n):
            x[i] -= m[i][j] * x[j]
        x[i] = x[i] / m[i][i]
    return x


# Calcula o vetor solução, para a matriz de uma equação, pelo método de Gauss.
# Entradas: q(x), r(x), malha de pontos, passo, número de pontos, y(a), y(b)
# Retorno: vetor solução
def v_sol_mh(q, r, x, h, n, a_, b_):
    # Calcula a matriz e o vetor de termos independentes
    m_h = construtor.matriz(q, x, h, n)
    v_h = construtor.vetor(r, x, h, n, a_, b_)

    # Calcula e retorna o vetor solução
    return v_sol(m_h, v_h, n - 1)


# Calcula o vetor solução, para a matriz de uma equação e diversos valores de n, pelo método de Gauss.
# Compara os valores solução do método de Gauss com a solução real.
# Plota o gráfico do erro máximo para cada valor de n.
# Entradas: y(x), q(x), r(x), extremo inicial (a), extremo final (b), y(a), y(b)
# Retorno: vetor com o erro máximo para cada valor de n.
def erro_n(y, q, r, a, b, a_, b_, n, n_step):
    # Erro entre valores obtidos pelo método de Gauss e a solução conhecida
    e = []
    # Erro máximo da cada iteração
    e_max = []

    for ni in range(5, n, n_step):
        # Calcula o passo adequado ao intervalo
        h = (b - a) / ni

        # Cria a malha de pontos
        x = []
        for i in range(1, ni):
            x.append(a + i * h)

        # Calcula o vetor solução real
        v_sol = solve.v_sol(y, x)

        # Calcula o vetor solução pelo método de Gauss
        v_gauss = v_sol_mh(q, r, x, h, ni, a_, b_)

        # Compara as soluções
        dif = [abs(i) for i in (np.array(v_sol) - np.array(v_gauss)).tolist()]
        e.append(dif)
        e_max.append(np.max(dif))
    return e_max

# ----------------teste----------------
if __name__ == "__main__":
    b = [[1, 2, 3], [4, 5, 8], [7, 8, 5]]
    c = [10, 11, 12]

    print(v_sol(b, c, 3))
