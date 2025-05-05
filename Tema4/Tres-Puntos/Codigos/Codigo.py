def derivada_tres_puntos(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
