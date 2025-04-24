def gauss_jordan(A, b):
    n = len(b)
    for i in range(n):
        factor = A[i][i]
        A[i] = A[i] / factor
        b[i] = b[i] / factor

        for j in range(n):
            if i != j:
                factor = A[j][i]
                A[j] -= factor * A[i]
                b[j] -= factor * b[i]
    return b