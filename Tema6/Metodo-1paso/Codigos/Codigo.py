def metodo_euler(f, y0, t0, tf, h):
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    while t < tf:
        y += h * f(t, y)
        t += h
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values