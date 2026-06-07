# Impacto del conflicto Rusia-Ucrania en los precios de alimentos en Europa (2020-2025)

## Descripción del proyecto

Este proyecto tiene como objetivo analizar la evolución de los precios de alimentos en Europa durante el período 2020-2025, considerando como contexto el conflicto Rusia-Ucrania y sus posibles efectos sobre la inflación alimentaria.

El análisis se desarrolla utilizando el conjunto de datos World Food Programme Global Food Prices Database, el cual contiene registros históricos de precios de productos alimentarios en distintos países. Para este proyecto, el estudio se delimita a países europeos, precios expresados en USD y productos alimentarios disponibles dentro del período de análisis.

Este repositorio corresponde a la Fase 1 del ABP, enfocada en la definición de la problemática, la organización inicial del entorno reproducible, la documentación técnica y la preparación del flujo de trabajo que será desarrollado en fases posteriores.

## Objetivo general

Analizar la evolución de los precios de alimentos en Europa durante el período 2020-2025 mediante herramientas de ciencia de datos, con el fin de identificar tendencias, diferencias entre países y posibles señales de inflación alimentaria asociadas al contexto del conflicto Rusia-Ucrania.

## Objetivos específicos

Organizar un entorno reproducible de trabajo mediante Git, GitHub, Jupyter Notebook y dependencias documentadas.
Cargar y revisar inicialmente los archivos de datos del World Food Programme correspondientes al período 2020-2025.
Identificar la estructura, dimensiones, tipos de variables y posibles problemas de calidad presentes en el dataset.
Definir criterios iniciales de filtrado, limpieza, validación y estandarización para las fases posteriores.
Documentar decisiones técnicas iniciales para asegurar trazabilidad y coherencia entre notebook, repositorio e informe.

## Dataset

Fuente de datos:

World Food Programme Global Food Prices Database

Criterios de filtrado del estudio:

Región: Europa.
Período: 2020-2025.
Moneda: USD.
Categoría: productos alimentarios.

Los archivos de datos se organizan por año y serán utilizados para construir una base consolidada que permita realizar análisis exploratorios y comparaciones temporales en fases posteriores.

## Tecnologías utilizadas

Python 3.12
Pandas
NumPy
Matplotlib
Jupyter Notebook
Git
GitHub

## Estructura del repositorio
```text
food-price-analysis/ 
│ 
├── README.md 
├── requirements.txt 
├── .gitignore 
│ 
└── F1/ 
    ├── data/ 
    │ ├── raw/ 
    │ └── processed/ 
    │ 
    ├── notebooks/ 
    │ └── F1_Definicion.ipynb 
    │ 
    ├── docs/ 
    │ 
    └── results/
```
## Descripción de carpetas y archivos

. README.md: documento principal del repositorio. Describe el proyecto, objetivos, dataset, tecnologías, estructura y forma de reproducir el entorno.

. requirements.txt: archivo que contiene las dependencias necesarias para ejecutar el proyecto en un entorno reproducible.

. F1/data/raw/: carpeta destinada a almacenar los archivos originales del dataset.

. F1/data/processed/: carpeta destinada a almacenar datos procesados o transformados en fases posteriores.

. F1/notebooks/: carpeta que contiene los notebooks reproducibles del proyecto.

. F1/docs/: carpeta destinada a documentación técnica, decisiones metodológicas, referencias y registros del proceso.

. F1/results/: carpeta destinada a resultados preliminares, tablas, gráficos o salidas generadas durante el análisis.


## Gestión de dependencias con requirements.txt

El archivo `requirements.txt` registra las librerías necesarias para ejecutar el proyecto en un entorno reproducible. Su función es permitir que cualquier integrante del equipo pueda reconstruir el ambiente de trabajo desde cero e instalar las mismas dependencias utilizadas durante la Fase 1.

En esta etapa, las dependencias principales son:

```text
pandas>=2.0
numpy>=2.0
matplotlib>=3.0
jupyter>=1.0
```

## Control de versiones

El proyecto utiliza Git y GitHub para asegurar trazabilidad y colaboración. La rama main se mantiene como versión estable del proyecto. Las modificaciones se realizan en ramas secundarias, como:

feature/fase1-fabian

Esta estrategia permite aislar los cambios, documentar avances mediante commits descriptivos y revisar las modificaciones antes de integrarlas a la rama principal mediante Pull Request.

Ejemplos de mensajes de commit utilizados o proyectados:

docs: mejora README con instrucciones de reproducibilidad
notebook: agrega decisiones tecnicas y validacion inicial
build: actualiza dependencias utilizadas en Fase 1
docs: registra limitaciones y supuestos del proyecto

## Decisiones técnicas iniciales

Durante la Fase 1 se definieron las siguientes decisiones técnicas:

Utilizar el dataset del World Food Programme por su cobertura internacional y disponibilidad de registros históricos.
Delimitar el análisis a países europeos para mantener coherencia con la problemática.
Considerar el período 2020-2025 para observar datos previos, contemporáneos y posteriores al inicio del conflicto.
Trabajar con precios en USD para facilitar la comparación entre países.
Documentar valores faltantes, duplicados, tipos de variables e inconsistencias antes de realizar transformaciones definitivas.
Mantener una estructura de carpetas que separe datos originales, datos procesados, notebooks, documentación y resultados.

## Limitaciones iniciales

En esta fase se reconocen algunas limitaciones preliminares:

La disponibilidad de datos puede variar entre países.
No todos los productos alimentarios tienen la misma frecuencia de registro.
Las variaciones de precios pueden estar influidas por factores distintos al conflicto Rusia-Ucrania, como inflación local, políticas públicas, costos energéticos o fluctuaciones cambiarias.
En Fase 1 no se establecen conclusiones causales, sino que se prepara el entorno técnico y metodológico para análisis posteriores.

