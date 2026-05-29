# Trabajo Práctico Integrador - Programación 1
### Gestión de Datos de Países 

## Integrantes
* **Daniela Esther Velazquez** (Desarrollo y Resolución Individual)
* **Nota de entrega:** El proyecto fue planificado inicialmente para ser desarrollado en equipo, pero ante la falta de comunicación y respuesta del compañero asignado, se asumió la totalidad del diseño, codificación y documentación de forma individual para garantizar los criterios de calidad académica.

## Institucion 
* **Universidad:** Universidad Tecnológica Nacional 
* **Carrera:** Tecnicatura Universitaria en Programación a distancia


## Descripción del Proyecto
Este sistema es una aplicación de consola desarrollada en Python 3.x que permite gestionar de manera integral un dataset de países. El programa lee, procesa y persiste los datos utilizando un archivo de formato abierto (.csv), implementando búsquedas dinámicas, filtros avanzados, ordenamientos eficientes y un módulo de analítica estadística.

El objetivo principal es aplicar de manera práctica los conceptos de **modularización**, **estructuras de datos compuestas** (listas de diccionarios), **control de excepciones** y **persistencia de datos**.


## Estructura del Repositorio
El código fuente se encuentra estrictamente modularizado bajo el principio de responsabilidad única:

* main.py: Punto de entrada de la aplicación. Maneja el menú interactivo por consola y la orquestación de los módulos.
* datos.py: Gestiona la persistencia de datos (lectura y escritura de archivos CSV) y la inicialización de la base de datos.
* busquedas.py: Contiene las funciones de búsqueda por coincidencia parcial y filtrado por rangos o categorías.
* ordenamientos.py: Implementa las funciones de ordenación del dataset mediante criterios dinámicos.
* estadisticas.py: Módulo analítico que calcula promedios, valores máximos, mínimos y distribución geográfica.
* validaciones.py: Asegura la robustez del sistema validando las entradas del usuario y previniendo errores en tiempo de ejecución.
* paises.csv: Archivo de texto que actúa como base de datos local.



## Instrucciones de Ejecución

Para ejecutar el sistema de manera local, asegúrese de tener instalado **Python 3.x** y siga estos pasos:

1. Clone el repositorio o descargue los archivos en una carpeta local:
   ```bash
   git clone [https://github.com/DanielaVelazquezDev/TPI_Programacion_1.git]
