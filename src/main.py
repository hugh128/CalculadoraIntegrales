import flet as ft
from integrales import calcular_integral_definida  # Importar la función

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
                        lower = float(lower)
                        upper = float(upper)
                        if lower > upper:
                            raise ValueError("El límite inferior no puede ser superior al límite superior.")
                    
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
            interval_field = ft.TextField(label="Intervalo de integración", width=400)
            result_text = ft.Text("Resultado: ", size=18)

            def calcular_area(e):
                result_text.value = "Funcionalidad aún no implementada"
                page.update()

            calculate_button = ft.ElevatedButton("Calcular", on_click=calcular_area)

            content_area.content = ft.Column([
                ft.Text("Área bajo la curva", size=18),
                input_field,
                interval_field,
                calculate_button,
                result_text
            ])

        elif pantalla == "Sólidos de revolución":
            input_field = ft.TextField(label="Ingrese la función", width=400)
            axis_field = ft.TextField(label="Eje de rotación", width=400)
            result_text = ft.Text("Resultado: ", size=18)

            def calcular_solido(e):
                result_text.value = "Funcionalidad aún no implementada"
                page.update()

            calculate_button = ft.ElevatedButton("Calcular", on_click=calcular_solido)

            content_area.content = ft.Column([
                ft.Text("Sólidos de revolución", size=18),
                input_field,
                axis_field,
                calculate_button,
                result_text
            ])

        elif pantalla == "Bienvenida":
            content_area.content = ft.Column([welcome_container])
        
        page.update()

    # Mensaje introductorio
    welcome_message = ft.Text(
        "Bienvenido a la Calculadora de Integrales. "
        "Seleccione una opción del menú para comenzar a calcular integrales, "
        "áreas bajo la curva o sólidos de revolución.",
        text_align="center",
        size=16
    )

    # Contenedor para el mensaje de bienvenida
    welcome_container = ft.Container(
        content=welcome_message,
        alignment=ft.alignment.center,
        width=500,
        padding=10
    )

    # Barra superior de la aplicación con ícono de "Home" a la izquierda
    app_bar = ft.AppBar(
        title=ft.Text("Calculadora de Integrales", text_align="center"),
        center_title=True,
        bgcolor=ft.colors.CYAN,
        leading=ft.IconButton(ft.icons.HOME, on_click=lambda e: actualizar_pantalla("Bienvenida"))  # Ícono a la izquierda
    )

    # Menú de navegación personalizado
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

    # Contenedor para el área de contenido inicial, con alineación centrada
    content_area = ft.Container(
        expand=True,  # Hace que el contenedor ocupe todo el espacio disponible
        alignment=ft.alignment.center,  # Centra el contenido tanto vertical como horizontalmente
        content=ft.Column([welcome_container]),  # Muestra el mensaje de bienvenida por defecto
        bgcolor=ft.colors.WHITE,
        padding=20
    )

    # Estructura de la página
    page.appbar = app_bar
    main_view = ft.Row(
        [nav_menu, content_area],
        expand=True
    )

    page.add(ft.Column([main_view], expand=True))

ft.app(main)
