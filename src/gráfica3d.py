import sympy as sp
import numpy as np
import plotly.graph_objects as go

# Función para calcular el volumen y graficar
def calcular_volumen():
    x = sp.symbols('x')
    
    # Entrada de datos del usuario
    funcion_str = input("Ingrese la función f(x): ")
    funcion = sp.sympify(funcion_str)
    
    lim_inf = float(input("Ingrese el límite inferior: "))
    lim_sup = float(input("Ingrese el límite superior: "))

    # Cálculo de volumen de revolución
    volumen = sp.integrate(sp.pi * funcion**2, (x, lim_inf, lim_sup))
    volumen_decimal = volumen.evalf()
    
    # Mostrar resultados
    print(f"Volumen del sólido de revolución (exacto): {volumen}")
    print(f"Volumen del sólido de revolución (aproximado): {volumen_decimal}")
    
    # Graficar el sólido de revolución con interactividad
    graficar_volumen(funcion, lim_inf, lim_sup)

# Función para graficar el volumen de revolución en 3D usando Plotly
def graficar_volumen(funcion, lim_inf, lim_sup):
    theta = np.linspace(0, 2 * np.pi, 100)
    x_vals = np.linspace(lim_inf, lim_sup, 100)
    X, T = np.meshgrid(x_vals, theta)
    Y = np.array([float(funcion.subs('x', x_val)) for x_val in x_vals])
    Z = Y * np.cos(T)
    W = Y * np.sin(T)

    # Crear la gráfica 3D interactiva con Plotly
    fig = go.Figure(data=[go.Surface(x=X, y=Z, z=W, colorscale="Viridis")])
    
    # Configuración de los ejes para hacerlos seleccionables e interactivos
    fig.update_layout(
        title="Sólido de revolución",
        scene=dict(
            xaxis=dict(title="X", showspikes=True, showline=True, showgrid=True),
            yaxis=dict(title="Y", showspikes=True, showline=True, showgrid=True),
            zaxis=dict(title="Z", showspikes=True, showline=True, showgrid=True),
        )
    )
    
    # Mostrar la gráfica interactiva
    fig.show()

calcular_volumen()
