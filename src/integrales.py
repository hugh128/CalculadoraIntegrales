# calculos/integrales.py
import sympy as sp

def calcular_integral_definida(funcion, limite_inferior=0, limite_superior=1):
    try:
        x = sp.symbols('x')
        # Convertir la expresión de texto a una función de sympy
        expr = sp.sympify(funcion)
        # Calcular la integral definida
        resultado = sp.integrate(expr, (x, limite_inferior, limite_superior))
        return resultado
    except Exception as e:
        raise ValueError(f"Error en el cálculo: {str(e)}")
