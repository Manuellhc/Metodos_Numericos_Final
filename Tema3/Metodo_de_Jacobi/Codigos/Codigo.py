import numpy as np

def jacobi(A, b, x0=None, tol=1e-6, max_iter=1000, verbose=False):
    """
    Resuelve el sistema Ax = b usando el método de Jacobi
    
    Parámetros:
    A: Matriz de coeficientes (n x n)
    b: Vector de términos independientes (n x 1)
    x0: Vector inicial (None para vector cero)
    tol: Tolerancia para el criterio de parada
    max_iter: Máximo número de iteraciones
    verbose: Mostrar información de iteraciones
    
    Retorna:
    x: Vector solución
    converged: Booleano indicando si convergió
    iterations: Número de iteraciones realizadas
    """
    n = len(A)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    x_new = np.zeros(n)
    
    # Verificar diagonal dominante (condición suficiente para convergencia)
    diagonal_dominant = all(2*np.abs(A[i,i]) >= np.sum(np.abs(A[i,:])) for i in range(n))
    if not diagonal_dominant and verbose:
        print("Advertencia: La matriz no es diagonal dominante - la convergencia no está garantizada")
    
    for iteration in range(max_iter):
        for i in range(n):
            s = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - s) / A[i, i]
        
        error = np.linalg.norm(x_new - x, np.inf)
        x = x_new.copy()
        
        if verbose:
            print(f"Iteración {iteration+1}: x = {x}, Error = {error:.6f}")
        
        if error < tol:
            return x, True, iteration+1
    
    return x, False, max_iter