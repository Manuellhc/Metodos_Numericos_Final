'''
Enunciado:
Analizar el error de redondeo y propagación al evaluar la función 𝑓(Z𝑥)=𝑒^𝑥 − 1  para un valor pequeño de 𝑥=0.1, usando redondeo a 5 cifras significativas.

Objetivo:
Mostrar cómo el redondeo afecta el resultado numérico y cómo se propaga el error en una operación compuesta.

'''

import math
import decimal

# Configurar la precisión decimal a 5 cifras significativas
decimal.getcontext().prec = 5

# Función para redondear un número a 5 cifras usando Decimal
def redondear(x):
    return float(decimal.Decimal(x))

# Definimos la función a evaluar: e^x - 1
def funcion(x):
    return math.exp(x) - 1

# Función principal para calcular errores
def calcular_errores(x):
    print(f"\nEvaluando en x = {x}")

    # Valor exacto (real) usando math.exp
    real = funcion(x)

    # Valor aproximado con redondeo
    aproximado = redondear(real)

    # Cálculo de error absoluto
    error = abs(real - aproximado)

    # Cálculo de error relativo (si el real no es 0)
    error_rel = abs(error / real) if real != 0 else 0

    # Imprimir resultados
    print(f"Valor real:       {real}")
    print(f"Valor redondeado: {aproximado}")
    print(f"Error absoluto:   {error}")
    print(f"Error relativo:   {error_rel}")

    # Simulación de propagación de errores:
    # Paso 1: calcular x² y redondearlo
    paso1 = redondear(x * x)

    # Paso 2: sumar x al resultado anterior y redondear
    paso2 = redondear(paso1 + x)

    # Mostrar pasos intermedios
    print(f"Propagación: Paso 1 = {paso1}, Paso 2 = {paso2}")

# Ejecutar el ejemplo funcional con x = 0.1
calcular_errores(0.1)

# Nota: No se incluyen entradas de usuario para evitar errores de datos.

'''
interpretación del resultado:
Aunque se usó redondeo a solo 5 cifras, el error absoluto es muy pequeño, lo cual indica que el redondeo fue aceptable para este caso.

El error relativo es menor a 1%, lo que también es bueno.

En las operaciones compuestas (propagación), los resultados se mantuvieron dentro de un rango controlado.

Este caso demuestra que con valores pequeños y control del redondeo, los errores numéricos pueden ser manejados sin afectar gravemente el resultado final.
'''
