import math

def cuadratura_gaussiana_2p(f, a, b):
    # Nodos y pesos para n=2 en [-1, 1]
    t1 = -1 / math.sqrt(3)
    t2 = 1 / math.sqrt(3)
    w1 = w2 = 1

    # Cambio de variable
    x1 = ((b - a) / 2) * t1 + (b + a) / 2
    x2 = ((b - a) / 2) * t2 + (b + a) / 2

    resultado = ((b - a) / 2) * (w1 * f(x1) + w2 * f(x2))
    return resultado
