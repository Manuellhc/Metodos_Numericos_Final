import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]  # Eliminación
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        suma = sum(A[i][j]*x[j] for j in range(i+1, n))
        x[i] = (b[i] - suma) / A[i][i]
    return x
