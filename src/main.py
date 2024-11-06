import flet as ft
from integrales import calcular_integral_definida
from solidos import generar_solido_revolucion, calcular_volumen_solido
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from flet.matplotlib_chart import MatplotlibChart
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart


def plot_function(func, lower, upper):
    x = sp.symbols('x')

    func_expr = sp.sympify(func)

    f = sp.lambdify(x, func_expr, 'numpy')

    x_vals = np.linspace(lower - (upper - lower) * 0.2, upper + (upper - lower) * 0.2, 1000)
    y_vals = f(x_vals)

    fig, ax = plt.subplots(figsize=(8, 6))

    margin = (upper - lower) * 0.2
    ax.set_xlim(lower - margin, upper + margin)
    ax.set_ylim(min(y_vals) - margin, max(y_vals) + margin)

    ax.plot(x_vals, y_vals, label=f'Función: {func}')

    x_fill = np.linspace(lower, upper, 100)
    y_fill = f(x_fill)
    ax.fill_between(x_fill, 0, y_fill, color='skyblue', alpha=0.5, label='Área bajo la curva')

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')

    ax.set_title('Gráfica de la función y área bajo la curva')

    ax.grid(True)
    ax.legend()

    return fig


def main(page: ft.Page):
    page.adaptive = True
    page.title = "Calculadora de Integrales"

    def actualizar_pantalla(pantalla):
        if pantalla == "Integral definida":
            input_field = ft.TextField(label="Ingrese la función", width=400)
            lower_limit = ft.TextField(label="Límite Inferior (opcional)", width=195)
            upper_limit = ft.TextField(label="Límite Superior (opcional)", width=195)
            result_text = ft.Text("Resultado: ", size=18)

            def calcular_integral(e):
                try:
                    func = input_field.value
                    lower = lower_limit.value if lower_limit.value else None
                    upper = upper_limit.value if upper_limit.value else None

                    if lower is not None and upper is not None:
                        lower = sp.sympify(lower)
                        upper = sp.sympify(upper)

                        if lower > upper:
                            result_text.value = "Error: El límite inferior no puede ser mayor que el límite superior."
                            result_text.color = ft.colors.RED
                            page.update()
                            return

                    if lower is None and upper is None:
                        integral_result = calcular_integral_definida(func)
                        integral_result_formatted = f"Integral indefinida: {integral_result}"
                    else:
                        integral_result = calcular_integral_definida(func, lower, upper)
                        integral_result_formatted = f"Resultado: {integral_result:.4f}"

                    result_text.value = integral_result_formatted
                    result_text.color = ft.colors.BLUE

                except ValueError as ve:
                    result_text.value = f"Error: {str(ve)}"
                    result_text.color = ft.colors.RED
                except Exception as e:
                    result_text.value = f"Error: {str(e)}"
                    result_text.color = ft.colors.RED

                page.update()

            calculate_button = ft.ElevatedButton("Calcular", on_click=calcular_integral)

            content_area.content = ft.Container(
                content=ft.Column([ 
                    ft.Text("Integral definida", size=18),
                    input_field,
                    ft.Row([lower_limit, upper_limit]),
                    calculate_button,
                    result_text
                ]),
                alignment=ft.alignment.center,
                width=500,
                padding=20
            )

        elif pantalla == "Área bajo la curva":
            input_field = ft.TextField(label="Ingrese la función", width=400)
            interval_field = ft.TextField(label="Intervalo de integración (por ejemplo, 0,2)", width=400)
            result_text = ft.Text("Resultado: ", size=18)
            chart = ft.Container(expand=True)

            def calcular_area(e):
                try:
                    func = input_field.value
                    interval = interval_field.value

                    if not interval:
                        raise ValueError("El intervalo no puede estar vacío.")
                    lower_limit, upper_limit = map(sp.sympify, interval.split(","))

                    if lower_limit > upper_limit:
                        result_text.value = "Error: El límite inferior no puede ser mayor que el límite superior."
                        result_text.color = ft.colors.RED
                        page.update()
                        return

                    x = sp.symbols('x')
                    func_expr = sp.sympify(func)
                    area = sp.integrate(func_expr, (x, lower_limit, upper_limit))
                    result_text.value = f"Área bajo la curva: {float(area):.4f}"
                    result_text.color = ft.colors.BLUE

                    fig = plot_function(func, float(lower_limit), float(upper_limit))
                    chart.content = MatplotlibChart(fig, expand=True)

                    page.update()

                except ValueError as ve:
                    result_text.value = f"Error: {str(ve)}"
                    result_text.color = ft.colors.RED
                    page.update()
                except Exception as e:
                    result_text.value = f"Error: {str(e)}"
                    result_text.color = ft.colors.RED
                    page.update()

            calculate_button = ft.ElevatedButton("Calcular", on_click=calcular_area)

            content_area.content = ft.Column(
                controls=[ 
                    ft.Text("Área bajo la curva", size=18),
                    input_field,
                    interval_field,
                    calculate_button,
                    result_text,
                    chart
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )

        elif pantalla == "Sólidos de revolución":
            input_field = ft.TextField(label="Ingrese la función", width=400)
            interval_field = ft.TextField(label="Intervalo de integración (por ejemplo, 0,2)", width=400)
            axis_field = ft.TextField(label="Eje de rotación (x o y)", width=400)
            result_text = ft.Text("Resultado: ", size=18)
            chart = ft.Container(expand=True)

            def calcular_solido(e):
                try:
                    func = input_field.value
                    interval = interval_field.value
                    eje_rotacion = axis_field.value.lower()

                    if not interval:
                        raise ValueError("El intervalo no puede estar vacío.")
                    if eje_rotacion not in ['x', 'y']:
                        raise ValueError("Eje de rotación inválido. Usa 'x' o 'y'.")
                    
                    lower_limit, upper_limit = map(float, interval.split(","))

                    volumen = calcular_volumen_solido(func, lower_limit, upper_limit, eje_rotacion)
                    result_text.value = f"Volumen del solido: {float(volumen):}"

                    fig = generar_solido_revolucion(func, lower_limit, upper_limit, eje_rotacion)
                    chart.content = MatplotlibChart(fig, expand=True)

                except ValueError as ve:
                        result_text.value = f"Error: {str(ve)}"
                        result_text.color = ft.colors.RED
                except Exception as e:
                        result_text.value = f"Error: {str(e)}"
                        result_text.color = ft.colors.RED
            
                page.update()
            
            calculate_button = ft.ElevatedButton("Calcular", on_click=calcular_solido)
            generate_3d_button = ft.ElevatedButton("Generar gráfica en 3D", on_click=calcular_solido)
            
            content_area.content = ft.Column(
                controls=[
                    ft.Text("Sólidos de revolución", size=18),
                    input_field,
                    interval_field,
                    axis_field,
                    calculate_button,
                    generate_3d_button,
                    result_text,
                    chart
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )


        elif pantalla == "Bienvenida":
            content_area.content = ft.Column([welcome_container])

        page.update()

    welcome_message = ft.Text(
        "Bienvenido a la Calculadora de Integrales. "
        "Seleccione una opción del menú para comenzar a calcular integrales, "
        "áreas bajo la curva o sólidos de revolución.",
        text_align="center",
        size=16
    )

    welcome_container = ft.Container(
        content=welcome_message,
        alignment=ft.alignment.center,
        width=500,
        padding=10
    )

    app_bar = ft.AppBar(
        title=ft.Text("Calculadora de Integrales", text_align="center"),
        center_title=True,
        bgcolor=ft.colors.CYAN,
        leading=ft.IconButton(ft.icons.HOME, on_click=lambda e: actualizar_pantalla("Bienvenida"))
    )

    nav_menu = ft.Container(
        width=220,
        bgcolor=ft.colors.GREY_200,
        padding=10,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.icons.FUNCTIONS, size=24),
                        ft.TextButton("Integral definida", on_click=lambda e: actualizar_pantalla("Integral definida"))
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.SHOW_CHART, size=24),
                        ft.TextButton("Área bajo la curva", on_click=lambda e: actualizar_pantalla("Área bajo la curva"))
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.THREED_ROTATION, size=24),
                        ft.TextButton("Sólidos de revolución", on_click=lambda e: actualizar_pantalla("Sólidos de revolución"))
                    ],
                    alignment=ft.MainAxisAlignment.START
                ),
            ],
            spacing=10
        )
    )

    content_area = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        padding=10
    )

    page.add(
        app_bar,
        ft.Row([nav_menu, content_area], expand=True)
    )

    actualizar_pantalla("Bienvenida")

ft.app(target=main)