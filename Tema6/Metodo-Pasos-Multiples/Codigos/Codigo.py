import math

def coeficiente_correlacion(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_y2 = sum(yi**2 for yi in y)
    sum_xy = sum(x[i]*y[i] for i in range(n))

    numerador = n * sum_xy - sum_x * sum_y
    denominador = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

    if denominador == 0:
        return 0  # Evitar división por cero

    r = numerador / denominador
    return r
