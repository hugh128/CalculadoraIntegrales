import sympy as sp

def calcular_integral_definida(funcion, limite_inferior=None, limite_superior=None):
    try:
        # Definir la variable simbólica
        x = sp.symbols('x')
        
        # Intentar convertir la expresión de texto a una expresión simbólica de sympy
        try:
            expr = sp.sympify(funcion)
        except sp.SympifyError:
            raise ValueError("La expresión ingresada no es válida. Asegúrese de usar una notación matemática correcta, por ejemplo, x**2 o sin(x).")
        
        # Verificar si la expresión es válida para el cálculo simbólico
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
    except ValueError as ve:
        raise ve  # Propaga el error de valor
    except Exception as e:
        raise Exception(f"Error al calcular la integral: {str(e)}")  # Manejo de cualquier otro error
