def f(x):
    return x**3 - x - 2  # Ejemplo

def regla_falsa(a, b, tol):
    if f(a)*f(b) >= 0:
        print("No se garantiza raíz en el intervalo")
        return None
    c = a
    while True:
        c = b - (f(b)*(a - b)) / (f(a) - f(b))
        if abs(f(c)) < tol:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
