#!/usr/bin/env python
# encoding: utf-8
# Método da bissecção ou dicotomia
import math
import numpy as np


def bissec(f, m1, m2, tol, crit_parada):
    tab = [["iter", "m1", "m2", "alpha", "f(alpha)"]]
    iter = 0
    bool_val = True
    while(bool_val):
        alpha = 0.5 * (m1 + m2)
        linha = [iter, m1, m2, alpha, f(alpha)]
        tab.append(linha)
        if f(alpha) * f(m1) < 0:
            m2 = alpha
        if f(alpha) * f(m1) > 0 or f(alpha) * f(m1) == 0:
            m1 = alpha
        iter += 1
        if crit_parada == 0:
            bool_val = (0.25 * abs(m1 - m2) > tol)
        elif crit_parada == 1:
            bool_val = (f(alpha - tol) * f(alpha + tol) > 0)
    return tab


# ----------------teste----------------
if __name__ == "__main__":

    print("teste1")

    def f(x):
        return 3 * math.pow(x, 3) - 2 * math.pow(x, 2) + 3 * x - 2

    tol = math.pow(10, -2)

    m1 = -1
    m2 = 1

    print(np.matrix(bissec(f, m1, m2, tol, 0)))

    print(np.matrix(bissec(f, m1, m2, tol, 1)))

    print("teste2")

    def f(x):
        return math.sin(x) - math.cos(x)

    tol = math.pow(10, -10)

    m1 = 0
    m2 = math.pi / 2  # a raíz da equação no intervalo desejado é pi/4

    print(np.matrix(bissec(f, m1, m2, tol, 0)))

    print(np.matrix(bissec(f, m1, m2, tol, 1)))

    # definindo novos limites
    m1 = 0
    m2 = 2

    print(np.matrix(bissec(f, m1, m2, tol, 0)))

    print(np.matrix(bissec(f, m1, m2, tol, 1)))