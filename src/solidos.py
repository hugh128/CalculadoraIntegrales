import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generar_solido_revolucion(funcion, limite_inferior, limite_superior, eje_rotacion='y'):
    x = sp.symbols('x')
    
    # Convertir la función a una expresión de SymPy
    try:
        expr = sp.sympify(funcion)
    except sp.SympifyError:
        raise ValueError("La expresión ingresada no es válida. Asegúrate de usar notación matemática correcta.")
    
    # Lambdify para convertir la expresión a una función NumPy
    f = sp.lambdify(x, expr, 'numpy')
    
    # Generar valores de x en el intervalo
    x_vals = np.linspace(limite_inferior, limite_superior, 100)
    y_vals = f(x_vals)
    
    # Configuración del gráfico 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    theta = np.linspace(0, 2 * np.pi, 100)
    theta_grid, x_grid = np.meshgrid(theta, x_vals)
    
    if eje_rotacion == 'y':
        X = x_grid
        Y = np.outer(y_vals, np.cos(theta))
        Z = np.outer(y_vals, np.sin(theta))
    elif eje_rotacion == 'x':
        Y = x_grid
        X = np.outer(y_vals, np.cos(theta))
        Z = np.outer(y_vals, np.sin(theta))
    else:
        raise ValueError("Eje de rotación inválido. Usa 'x' o 'y'.")
    
    ax.plot_surface(X, Y, Z, color='skyblue', edgecolor='k', alpha=0.5)
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title(f"Sólido de revolución alrededor del eje {eje_rotacion}")

    return fig

import sympy as sp

def calcular_volumen_solido(func, lower, upper, eje_rotacion):
    x = sp.symbols('x')
    func_expr = sp.sympify(func)
    if eje_rotacion == 'x':
        volume = sp.pi * sp.integrate(func_expr**2, (x, lower, upper))
    else:
        volume = sp.pi * sp.integrate((func_expr)**2, (x, lower, upper))
    return volume

