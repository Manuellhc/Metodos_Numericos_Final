def interpolacion_lineal(x0, y0, x1, y1, x):
    if x0 == x1:
        raise ValueError("x0 y x1 no pueden ser iguales.")
    pendiente = (y1 - y0) / (x1 - x0)
    return y0 + pendiente * (x - x0)
