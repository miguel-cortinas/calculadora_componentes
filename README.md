# Calculadora Modular

Este proyecto es una implementación de una calculadora modular en Python, siguiendo los principios de Ingeniería de Software basada en componentes. La calculadora está dividida en componentes independientes para realizar operaciones matemáticas básicas como suma, resta, multiplicación y división.

## Estructura del Proyecto

El proyecto está organizado en varios archivos para cada componente:

-   `suma.py`: Contiene la función para realizar la operación de suma.
-   `resta.py`: Contiene la función para realizar la operación de resta.
-   `multiplicacion.py`: Contiene la función para realizar la operación de multiplicación.
-   `division.py`: Contiene la función para realizar la operación de división.
-   `calculadora.py`: Es el archivo principal que contiene el menú y la lógica para utilizar los componentes.

## Uso

Para utilizar la calculadora, ejecuta el archivo `calculadora.py` en tu entorno de Python. Asegúrate de tener Python instalado en tu sistema.

    python calculadora.py

Al ejecutar el programa, se mostrará un menú con las siguientes opciones:

1.  **Suma**
2.  **Resta**
3.  **Multiplicación**
4.  **División**
5.  **Salir**

Selecciona el número correspondiente a la operación que deseas realizar e ingresa los números cuando se te pida. El programa calculará el resultado utilizando los componentes específicos para cada operación y mostrará el resultado en la pantalla.

## Principios de Ingeniería de Software basada en componentes

Este proyecto sigue el enfoque de Ingeniería de Software basada en componentes, dividiendo las funcionalidades en componentes independientes reutilizables. Cada operación matemática (suma, resta, multiplicación y división) se implementa como un componente separado, lo que facilita su mantenimiento y mejora la modularidad del sistema en su conjunto.