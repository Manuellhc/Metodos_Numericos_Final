'''
Enunciado:
Evaluar la función 𝑓(𝑥)=𝑒^𝑥−1 con un modelo matemático pobre y datos inválidos para simular errores de modelado y de entrada.

Objetivo:
Mostrar cómo errores de modelado (una mala aproximación de la función) y errores en la entrada pueden afectar negativamente el resultado numérico.

'''

import math

def entrada_con_error(valor):
    try:
        return float(valor)
    except:
        print("¡Error de datos: entrada inválida!")
        return None

def modelo_pobre(x):
    # Aproximación muy simple: e^x ≈ 1 + x
    return x

x1 = entrada_con_error("abc")  # entrada inválida

x2 = 0.5
real = math.exp(x2) - 1
aprox = modelo_pobre(x2)

print(f"\nModelo pobre con x = {x2}")
print(f"Valor real:  {real}")
print(f"Aproximado:  {aprox}")
print(f"Error modelado: {abs(real - aprox)}")

# Nota: No se incluyen entradas de usuario para evitar errores de datos.

'''
interpretación del resultado:
El intento de convertir "abc" a número falló, generando un error de datos (dato mal ingresado).
El modelo f(x)=x es una mala aproximación de 𝑒^𝑥−1, especialmente para valores medianos como 𝑥=0.5.
El error de modelado es significativo (≈0.15), lo cual demuestra que usar modelos incorrectos puede llevar a resultados numéricos muy alejados de la realidad.
'''
