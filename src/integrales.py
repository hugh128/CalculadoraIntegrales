import sympy as sp
import re
from typing import Union, Optional

def calcular_integral_definida(funcion: str, limite_inferior: Optional[Union[int, float]] = None, 
                             limite_superior: Optional[Union[int, float]] = None) -> Union[str, float]:

    def sympify_func(func: str) -> sp.Basic:
        func = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', func)
        
        def process_sqrt(match):
            inner = match.group(1)
            inner = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', inner)
            return f'sqrt({inner})'
        
        func = re.sub(r'sqrt\((.*?)\)', process_sqrt, func)
        
        # Paso 3: Reemplazos comunes
        replacements = {
            '^': '**',
            'sqrt': 'sp.sqrt',
            'sin': 'sp.sin',
            'cos': 'sp.cos',
            'tan': 'sp.tan',
            'exp': 'sp.exp',
            'log': 'sp.log',
            'pi': 'sp.pi',
            'e': 'sp.E'
        }
        
        for old, new in replacements.items():
            func = func.replace(old, new)
        
        func = re.sub(r'\)(\w)', r')*\1', func)
        
        try:
            return sp.sympify(func)
        except (sp.SympifyError, TypeError) as e:
            error_msg = str(e)
            if "sqrt" in func.lower():
                sugerencia = "\nSugerencia: Para raíz cuadrada, asegúrese de que la expresión dentro de sqrt() es válida."
                if "4x" in func:
                    sugerencia += "\nPor ejemplo, use 'sqrt(4*x)' en lugar de 'sqrt(4x)'"
            else:
                sugerencia = "\nUse notación como: x**2, sin(x), 2*x, etc."
            raise ValueError(f"Expresión matemática inválida: {error_msg}{sugerencia}")

    def validar_limites(inf: Optional[Union[int, float]], 
                       sup: Optional[Union[int, float]]) -> tuple[Optional[float], Optional[float]]:
        if inf is not None and sup is not None:
            try:
                inf_float = float(inf)
                sup_float = float(sup)
                if inf_float >= sup_float:
                    raise ValueError("El límite inferior debe ser menor que el superior")
                return inf_float, sup_float
            except ValueError as e:
                if "must be menor" in str(e):
                    raise e
                raise ValueError("Los límites deben ser números válidos")
        return inf, sup

    try:
        x = sp.Symbol('x')
        
        expr = sympify_func(funcion)
        
        if not isinstance(expr, sp.Basic):
            raise ValueError("La expresión no es válida para integración")
            
        limite_inferior, limite_superior = validar_limites(limite_inferior, limite_superior)
        
        if limite_inferior is None or limite_superior is None:
            resultado = sp.integrate(expr, x)
            return f"{sp.latex(resultado)} + C"
        else:
            resultado = sp.integrate(expr, (x, limite_inferior, limite_superior))
            return float(resultado.evalf())
            
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise Exception(f"Error durante el cálculo: {str(e)}")
