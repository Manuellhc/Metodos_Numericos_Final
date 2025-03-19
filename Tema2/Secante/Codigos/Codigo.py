def f(x):
    return x**3 - x - 2  # Ejemplo

def secante(x0, x1, tol):
    while abs(f(x1)) > tol:
        try:
            x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        except ZeroDivisionError:
            print("Error: División por cero en secante.")
            return None
        x0, x1 = x1, x2
    return x1
