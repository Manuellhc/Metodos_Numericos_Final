def f(x):
    return x**3 - x - 2  # Ejemplo de función

def biseccion(a, b, tol):
    if f(a) * f(b) >= 0:
        print("No se garantiza una raíz en el intervalo.")
        return None
    while (b - a)/2 > tol:
        c = (a + b)/2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Ejemplo de uso
raiz = biseccion(1, 2, 0.0001)
print("La raíz aproximada es:", raiz)
