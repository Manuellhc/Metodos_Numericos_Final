TEMA 1: Fundamentos de Métodos Numéricos

[Carpeta tema1](https://github.com/Manuellhc/Metodos_Numericos_Final/tree/main/Tema1)

    Los métodos numéricos son herramientas matemáticas que permiten encontrar soluciones aproximadas a problemas complejos que no pueden resolverse analíticamente. Estudian procedimientos algorítmicos que permiten obtener valores aproximados de soluciones a problemas matemáticos como ecuaciones algebraicas, integrales, derivadas, etc.

    Subtemas:

    Error Absoluto y Relativo: Se usan para medir la precisión de los resultados. El error absoluto es la diferencia entre el valor real y el valor aproximado. El error relativo es el cociente entre el error absoluto y el valor real.

    Cifras Significativas: Son los dígitos correctos de un número que representan información precisa. Son esenciales para reportar resultados numéricos con la precisión adecuada.

    Propagación del Error: Describe cómo los errores se transmiten a través de operaciones matemáticas, especialmente en cadenas de cálculos.

    Condicionamiento y Estabilidad: El condicionamiento indica qué tan sensible es un problema al error en los datos de entrada. La estabilidad se refiere a la sensibilidad del algoritmo al error de redondeo.

TEMA 2: Solución Numérica de Ecuaciones
[Carpeta tema2](https://github.com/Manuellhc/Metodos_Numericos_Final/tree/main/Tema2)

    Trata sobre encontrar aproximaciones para las raíces de ecuaciones no lineales.

    Subtemas:

    Método de Bisección: Divide el intervalo a la mitad. Es seguro pero lento.

    Método de Newton-Raphson: Usa derivadas para converger rápidamente, pero necesita una buena estimación inicial.

    Método de la Secante: Aproxima la derivada y mejora en velocidad al de bisección.

    Método de Punto Fijo: Requiere transformar la ecuación en x = g(x). Puede no converger si g(x) no está bien elegida.

TEMA 3: Sistemas de Ecuaciones Lineales
[Carpeta tema3](https://github.com/Manuellhc/Metodos_Numericos_Final/tree/main/Tema3)

    Permite resolver sistemas de la forma Ax = b, donde A es una matriz de coeficientes.

    Subtemas:

    Eliminación Gaussiana: Reduce el sistema a forma escalonada para resolver con sustitución regresiva.

    Método de Gauss-Jordan: Lleva la matriz a forma escalonada reducida. Ideal para encontrar la inversa.

    Método de Jacobi: Método iterativo que parte de una estimación inicial.

    Método de Gauss-Seidel: Similar al Jacobi pero mejora la convergencia utilizando los valores recientes en cada iteración.

TEMA 4: Diferenciación e Integración Numérica
[Carpeta tema4](https://github.com/Manuellhc/Metodos_Numericos_Final/tree/main/Tema4)

    Permite calcular derivadas e integrales cuando no es posible hacerlo analíticamente.

    Subtemas:

    Fórmula de Tres Puntos: Estima la derivada en un punto usando dos vecinos. Precisa y sencilla para funciones suaves.

    Fórmula de Cinco Puntos: Proporciona una aproximación más precisa a la derivada al usar cinco valores.

    Método del Trapecio: Aproxima el área bajo la curva con trapecios. Sencillo y rápido.

    Regla de Simpson: Usa parábolas para aproximar el área. Mayor precisión para funciones suaves.

    Cuadratura Gaussiana: Usa puntos y pesos óptimos para integrar con gran precisión, incluso con pocos puntos.

TEMA 5: Interpolación y Ajuste de Funciones
[Carpeta tema5](https://github.com/Manuellhc/Metodos_Numericos_Final/tree/main/Tema5)

    Busca obtener funciones que representen un conjunto de datos.

    Subtemas:

    Interpolación Lineal: Une puntos con rectas. Es sencilla, pero puede no ser suave.

    Interpolación Polinómica: Ajusta un polinomio que pasa por todos los puntos. Problemas de oscilación si hay muchos datos.

    Métodos de Regresión: Encuentran la mejor curva que se ajusta a datos experimentales. Incluye regresión lineal, cuadrática, etc.

    Correlación y Mínimos Cuadrados: Evalúa la relación entre variables y ajusta funciones minimizando el error cuadrático.

TEMA 6: Solución de Ecuaciones Diferenciales Ordinarias (EDO)
[Carpeta tema6](https://github.com/Manuellhc/Metodos_Numericos_Final/tree/main/Tema6)

    Permite modelar fenómenos dinámicos como el crecimiento poblacional o el movimiento de un péndulo.

    Subtemas:

    Métodos de un Paso: Calculan el siguiente valor de la solución usando solo el valor actual. Ejemplo: Método de Euler.

    Método de Pasos Múltiples: Utiliza varios puntos anteriores para calcular el siguiente. Ejemplo: Adams-Bashforth.

    Método de Euler para Sistemas de EDOs: Extiende Euler para resolver sistemas de ecuaciones diferenciales, resolviendo cada variable simultáneamente paso a paso.

Conclusión General:

    Los métodos numéricos permiten abordar problemas reales de ingeniería y ciencias que serían difíciles o imposibles de resolver analíticamente. Aunque implican un cierto margen de error, su eficacia radica en su aplicabilidad, rapidez computacional y adaptabilidad a diversos contextos prácticos. Comprender cada método, sus ventajas, limitaciones y cómo y cuándo aplicarlo, es esencial para el éxito en la resolución de problemas científicos y técnicos.



    
![alt text](image.png)