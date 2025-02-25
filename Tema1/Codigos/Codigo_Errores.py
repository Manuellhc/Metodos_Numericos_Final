import math
import decimal

# Configurar precisión decimal
decimal.getcontext().prec = 5  # solo 5 cifras significativas

def funcion(x):
    """Función a evaluar"""
    return math.exp(x) - 1  # Modelo matemático simplificado

def valor_real(x):
    """Valor real (usando más precisión)"""
    return math.e**x - 1

def redondear(x):
    """Simulación de error de redondeo"""
    return float(decimal.Decimal(x))

def calcular_errores(x):
    print(f"\nEvaluando en x = {x}")
    real = valor_real(x)
    aproximado = redondear(funcion(x))

    error_exactitud = abs(real - aproximado)
    error_relativo = abs(error_exactitud / real) if real != 0 else 0

    print(f"Valor real:       {real}")
    print(f"Valor redondeado: {aproximado}")
    print(f"Error exactitud:  {error_exactitud}")
    print(f"Error relativo:   {error_relativo}")

    # Simular propagación con 2 pasos
    paso1 = redondear(x * x)
    paso2 = redondear(paso1 + x)
    print(f"Propagación: Paso 1 = {paso1}, Paso 2 = {paso2}")

# Datos erróneos (error de datos)
def entrada_con_error(x_str):
    try:
        x = float(x_str)
        return x
    except:
        print("¡Error de datos: entrada inválida!")
        return None
