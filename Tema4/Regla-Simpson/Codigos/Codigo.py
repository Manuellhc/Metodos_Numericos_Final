def regla_simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de intervalos (n) debe ser par.")

    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)

    return (h / 3) * suma
