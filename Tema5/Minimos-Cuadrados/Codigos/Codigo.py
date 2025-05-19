def ajuste_minimos_cuadrados(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum(xi**2 for xi in x)
    sum_xy = sum(x[i]*y[i] for i in range(n))

    denominador = n * sum_x2 - sum_x**2
    if denominador == 0:
        raise ValueError("Denominador cero, no se puede calcular la regresión")

    b = (n * sum_xy - sum_x * sum_y) / denominador
    a = (sum_y / n) - b * (sum_x / n)

    return a, b
