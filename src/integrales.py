# calculos/integrales.py
import sympy as sp

def calcular_integral_definida(funcion, limite_inferior=None, limite_superior=None):
    try:
        # Definir la variable simbólica
        x = sp.symbols('x')
        
        # Convertir la expresión de texto a una expresión de sympy
        expr = sp.sympify(funcion)
        
        # Verificar si la expresión es válida
        if not isinstance(expr, sp.Basic):
            raise ValueError("La expresión ingresada no es válida para cálculo simbólico.")
        
        # Si no se proporcionan límites, se calcula la integral indefinida
        if limite_inferior is None and limite_superior is None:
            resultado = sp.integrate(expr, x)  # Integral indefinida
            resultado = f"{resultado} + C"  # Se agrega la constante de integración
        else:
            # Si se proporcionan límites, calcular la integral definida
            limite_inferior = float(limite_inferior) if limite_inferior else 0
            limite_superior = float(limite_superior) if limite_superior else 1
            resultado = sp.integrate(expr, (x, limite_inferior, limite_superior))  # Integral definida
        
        return resultado
    except sp.SympifyError:
        raise ValueError("La expresión ingresada no es válida. Asegúrese de usar una notación correcta.")
    except Exception as e:
        raise ValueError(f"Error en el cálculo de la integral: {str(e)}")
