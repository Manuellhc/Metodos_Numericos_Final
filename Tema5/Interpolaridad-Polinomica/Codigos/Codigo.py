# Método de interpolación de Lagrange
def interpolacion_lagrange(x_puntos, y_puntos, x):
    total = 0
    n = len(x_puntos)
    for j in range(n):
        term = y_puntos[j]
        for m in range(n):
            if m != j:
                term *= (x - x_puntos[m]) / (x_puntos[j] - x_puntos[m])
        total += term
    return total
