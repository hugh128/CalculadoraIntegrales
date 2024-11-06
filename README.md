# Proyecto: Calculadora de Integrales, Áreas y Sólidos de Revolución

Este proyecto permite realizar cálculos de integrales y visualizaciones gráficas de areas bajo la curva y sólidos de revolución. Con él, los usuarios pueden calcular integrales de funciones matemáticas, generar y visualizar sólidos de revolución a partir de curvas, y obtener el volumen de estos sólidos mediante integración. Utiliza bibliotecas como SymPy para cálculos simbólicos, NumPy para manipulación de datos y Matplotlib para gráficos en 3D.

## Descripción General

La generación de sólidos de revolución es un concepto fundamental en cálculo integral, donde se calcula el volumen de un sólido obtenido al rotar una curva alrededor de un eje. Este proyecto automatiza y visualiza este proceso, facilitando la comprensión y el análisis de estos sólidos. La funcionalidad del proyecto permite:

- **Calcular integrales** (definidas e indefinidas) de funciones en términos de una variable.
- **Generar sólidos de revolución** en un gráfico 3D, rotando una función alrededor de los ejes `x` o `y`.
- **Calcular el volumen del sólido** generado a partir de la rotación de una curva en un intervalo definido.

## Características

- **Cálculo de Integrales**: Utilizando el módulo `integrales.py`, el proyecto permite calcular integrales definidas y añadir una constante a integrales indefinidas, proporcionando flexibilidad en el análisis matemático.
- **Visualización 3D de Sólidos de Revolución**: Con el módulo `solidos.py`, puedes graficar sólidos en 3D, eligiendo entre los ejes `x` o `y` como eje de rotación. Esto facilita la visualización y comprensión de cómo una función se transforma en un sólido.
- **Cálculo Simbólico del Volumen**: El proyecto permite calcular el volumen exacto del sólido de revolución mediante integración simbólica, proporcionando un resultado preciso y rápido.
- **Fácil Configuración de Límites**: Los usuarios pueden establecer límites inferiores y superiores de integración y generación de sólidos, lo cual es útil para estudiar porciones específicas de una función.
- **Interfaz Flexible**: La estructura modular del proyecto facilita su uso y extensión, permitiendo integrar funciones de cálculo y visualización en otros proyectos de matemáticas o ingeniería.

## Estructura del Proyecto

El proyecto consta de los módulos principales:

1. `integrales.py`: Calcula integrales definidas e indefinidas.
2. `solidos.py`: Genera el gráfico 3D de un sólido de revolución y calcula su volumen.
3. `main.py`: Para ejecutar la aplicacion usando flet como framework.

## Requisitos

Para ejecutar el proyecto, se necesita Python 3.8 o superior y las siguientes bibliotecas:

- `SymPy`: Para cálculos simbólicos.
- `NumPy`: Para manipulación de matrices y cálculo numérico.
- `Matplotlib`: Para graficar sólidos de revolución en 3D.
- `Flet`: Para marco de interfaz de usuario.
- `plotly`: Para gráficos interactivos.

## Screenshots
- Pantalla inicial

![](/screenshots/home.png)

- Integral definida
![](/screenshots/integral.png)

- Area bajo la curva
![](/screenshots/area_bajo_curva.png)

- Solidos de revolución
![](/screenshots/solido_de_revolusion.png)

## Créditos

Este proyecto fue desarrollado como parte del curso de calculo ll con fines educativos.

## Autores

- Pablo Cobon (2690-23-18351)
- Hugo Ordoñez (2690-23-10929)
- Juan Carlos Ochoa
