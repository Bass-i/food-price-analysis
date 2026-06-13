# Impacto del conflicto Rusia-Ucrania en los precios de los alimentos en Europa (2020-2025)

## Descripción del proyecto

Este proyecto académico tiene como objetivo analizar la evolución de los precios de alimentos en Europa durante el período 2020-2025, considerando como contexto el conflicto Rusia-Ucrania y sus posibles efectos sobre los mercados alimentarios.

El análisis utiliza información proveniente de la base de datos **World Food Programme Global Food Prices Database (WFP)**. El proyecto se desarrolla progresivamente mediante las fases definidas en la asignatura **MCDI500 — Herramientas de software científico**, incorporando procesos de definición del problema, obtención de datos, limpieza, transformación, validación, análisis algorítmico, medición de eficiencia y Programación Orientada a Objetos en Python.

El desarrollo se organiza en tres fases principales:

* **Fase 1:** definición del problema, objetivos, estructura del proyecto y entorno reproducible.
* **Fase 2:** obtención, consolidación, limpieza, transformación y validación del dataset.
* **Fase 3:** construcción del núcleo algorítmico mediante programación estructurada, recursividad, medición de complejidad y Programación Orientada a Objetos.

---

## Integrantes

* Franco Reyes Koch
* Renato Villazón Martínez
* Fabian Castillo Rojas

---

## Objetivo general

Analizar la evolución de los precios de alimentos en países europeos disponibles dentro del conjunto de datos del WFP durante el período 2020-2025, con el fin de identificar tendencias, variaciones y posibles efectos asociados al contexto del conflicto Rusia-Ucrania.

---

## Objetivos específicos

* Configurar un entorno reproducible utilizando Python, Git, GitHub y Jupyter Notebook.
* Consolidar archivos de datos correspondientes al período 2020-2025.
* Realizar procesos de limpieza, transformación y validación del conjunto de datos.
* Filtrar los países europeos disponibles dentro de la cobertura del WFP.
* Generar un dataset procesado que sirva como base para fases posteriores.
* Diseñar funciones y algoritmos para analizar variaciones en los precios de alimentos.
* Implementar un algoritmo recursivo y medir su eficiencia computacional.
* Refactorizar parte del flujo de análisis hacia una arquitectura orientada a objetos.
* Aplicar principios de encapsulamiento, herencia y polimorfismo en el núcleo algorítmico del proyecto.
* Documentar el proceso técnico mediante notebooks, scripts, comentarios, docstrings y control de versiones.

---

## Dataset

### Fuente de datos

**World Food Programme Global Food Prices Database (WFP)**

### Período analizado

2020-2025

### Variables principales

* País (`countryiso3`)
* Fecha (`date`)
* Región administrativa (`admin1`, `admin2`)
* Mercado (`market`)
* Categoría (`category`)
* Producto (`commodity`)
* Moneda (`currency`)
* Unidad de medida (`unit`)
* Precio local (`price`)
* Precio en dólares estadounidenses (`usdprice`)
* Latitud (`latitude`)
* Longitud (`longitude`)

La variable principal para el análisis comparativo es `usdprice`, ya que permite comparar precios entre países utilizando una moneda común.

---

## Tecnologías utilizadas

* Python 3.12
* Pandas
* NumPy
* Jupyter Notebook
* Git
* GitHub
* Módulos estándar de Python:

  * `pathlib`
  * `timeit`
  * `abc`

---

## Estructura del repositorio

```text
food-price-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
│
│
├── F1/
│   ├── data/
│   │   ├── wfp_food_prices_global_2020.csv
│   │   ├── wfp_food_prices_global_2021.csv
│   │   ├── wfp_food_prices_global_2022.csv
│   │   ├── wfp_food_prices_global_2023.csv
│   │   ├── wfp_food_prices_global_2024.csv
│   │   └── wfp_food_prices_global_2025.csv
│   │
│   ├── notebooks/
│   │   └── F1_Definicion.ipynb
│   ├── docs/
│   └── results/
│
├── F2/
│   ├── data/
│   │   └── processed/
│   │       └── wfp_europe_2020_2025_clean.csv
│   ├── notebooks/
│   │   └── F2_Preprocesamiento.ipynb
│   ├── docs/
│   ├── results/
│   └── src/
│
└── F3/
    ├── data/
    │   └── wfp_europe_2020_2025_clean.csv
    ├── notebooks/
    │   └── F3_Nucleo_Algoritmico.ipynb
    ├── src/
    │   ├── preprocesador.py
    │   ├── analizador.py
    │   ├── algoritmos.py
    │   └── pipeline.py
    ├── docs/
    └── results/
```

---

## Fase 1: Definición del proyecto

Durante la Fase 1 se definió la problemática central del proyecto, relacionada con la evolución de los precios de alimentos en Europa durante el período 2020-2025 y el contexto del conflicto Rusia-Ucrania.

En esta etapa se desarrollaron las siguientes actividades:

* Definición de la problemática.
* Formulación de la pregunta de investigación.
* Definición del objetivo general y objetivos específicos.
* Configuración inicial del entorno de trabajo.
* Creación de la estructura base del repositorio.
* Creación del notebook inicial del proyecto.
* Documentación inicial en `README.md`.
* Definición de dependencias en `requirements.txt`.

### Notebook principal

```text
F1/notebooks/F1_Definicion.ipynb
```

---

## Fase 2: Preprocesamiento y validación de datos

Durante la Fase 2 se implementó un pipeline reproducible de obtención, limpieza, transformación y validación de datos. Esta fase permitió generar un dataset procesado que sirve como base para las fases posteriores del proyecto.

Las principales actividades realizadas fueron:

* Carga automatizada de archivos CSV anuales.
* Consolidación de datos del período 2020-2025.
* Diagnóstico inicial del dataset.
* Revisión de duplicados.
* Revisión de valores faltantes.
* Conversión de la variable `date` a formato de fecha.
* Creación de variables temporales `year` y `month`.
* Filtrado de países europeos disponibles en la base.
* Eliminación de registros con valores nulos en `usdprice`.
* Conservación justificada de nulos en variables geográficas no críticas.
* Validación técnica del dataset resultante.
* Exportación del dataset limpio.

### Notebook principal

```text
F2/notebooks/F2_Preprocesamiento.ipynb
```

### Dataset procesado generado

```text
F2/data/processed/wfp_europe_2020_2025_clean.csv
```

El dataset procesado queda compuesto por registros europeos disponibles en la base WFP durante el período 2020-2025. Este archivo constituye la entrada principal para la Fase 3.

---

## Fase 3: Núcleo algorítmico y Programación Orientada a Objetos

La Fase 3 se construye sobre el dataset procesado en la Fase 2. Por este motivo, no se vuelve a ejecutar la limpieza completa desde los archivos raw. En cambio, se reutiliza el archivo `wfp_europe_2020_2025_clean.csv` y se encapsulan en clases las operaciones necesarias para preparar, validar y analizar los datos.

El foco de esta etapa está en el diseño algorítmico, la eficiencia computacional y la Programación Orientada a Objetos.

### Objetivo de la Fase 3

Construir un núcleo algorítmico modular y reproducible para analizar variaciones en los precios de alimentos, aplicando programación estructurada, recursividad, medición de complejidad y Programación Orientada a Objetos.

### Notebook principal

```text
F3/notebooks/F3_Nucleo_Algoritmico.ipynb
```

### Scripts principales

```text
F3/src/preprocesador.py
F3/src/analizador.py
F3/src/algoritmos.py
F3/src/pipeline.py
```

---

## Arquitectura de Fase 3

La arquitectura de Fase 3 se organiza en módulos con responsabilidades separadas:

| Archivo            | Componente                   | Responsabilidad                                                                          |
| ------------------ | ---------------------------- | ---------------------------------------------------------------------------------------- |
| `preprocesador.py` | `Preprocesador`              | Cargar el dataset procesado de Fase 2 y preparar los datos para el análisis algorítmico. |
| `analizador.py`    | `AnalizadorBase`             | Definir una clase base para los analizadores del proyecto.                               |
| `analizador.py`    | `AnalizadorVariacionPrecios` | Calcular precios promedio anuales y variaciones porcentuales por producto.               |
| `analizador.py`    | `AnalizadorEstadistico`      | Generar estadísticas descriptivas sobre la variable `usdprice`.                          |
| `algoritmos.py`    | `merge_sort`                 | Implementar un algoritmo recursivo de ordenamiento.                                      |
| `pipeline.py`      | `PipelineAnalisis`           | Coordinar la ejecución completa del flujo de análisis.                                   |

---

## Programación Orientada a Objetos en Fase 3

En esta fase se incorporan principios de Programación Orientada a Objetos para mejorar la organización, reutilización y mantenibilidad del código.

### Encapsulamiento

El encapsulamiento se aplica manteniendo atributos internos protegidos, como `_df` y `_ruta_csv`, dentro de las clases. Esto permite controlar el acceso al estado interno del objeto y evitar modificaciones accidentales desde fuera de la clase.

### Herencia

La clase `AnalizadorBase` funciona como clase base para distintos tipos de analizadores. A partir de ella se crean clases especializadas como:

* `AnalizadorVariacionPrecios`
* `AnalizadorEstadistico`

Estas clases reutilizan la estructura común definida en la clase base y especializan el comportamiento según el tipo de análisis.

### Polimorfismo

El polimorfismo se aplica mediante el método común `analizar()`. Cada clase hija implementa este método de forma diferente:

* `AnalizadorVariacionPrecios.analizar()` calcula variaciones anuales de precios.
* `AnalizadorEstadistico.analizar()` genera estadísticas descriptivas.

Esto permite ejecutar distintos analizadores mediante una interfaz común.

---

## Algoritmo recursivo

La Fase 3 incluye una implementación del algoritmo `merge_sort`, utilizado como ejemplo de recursividad y estrategia de divide y vencerás.

El algoritmo se compone de:

* Caso base: listas de tamaño menor o igual a 1.
* Caso recursivo: división de la lista en dos mitades.
* Fusión de resultados: combinación ordenada de las listas parciales.

Este algoritmo permite evidenciar el uso de recursividad dentro del proyecto y analizar su eficiencia computacional.

---

## Eficiencia y optimización

En el notebook de Fase 3 se realizan mediciones de tiempo utilizando `timeit`, comparando la implementación recursiva de `merge_sort` con la función nativa `sorted()` de Python.

La comparación permite observar diferencias de rendimiento entre una implementación académica en Python puro y una función interna optimizada del lenguaje.

Aunque ambos enfoques presentan una complejidad temporal promedio de orden `O(n log n)`, `sorted()` suele ser más eficiente en la práctica debido a que utiliza una implementación altamente optimizada.



## Ejecución de Fase 3

Desde el notebook de Fase 3 se importan los módulos ubicados en `F3/src/` y se ejecuta el flujo principal del análisis.

Ejemplo general:

```python
from pipeline import PipelineAnalisis

pipeline = PipelineAnalisis("../data/wfp_europe_2020_2025_clean.csv")

variaciones, estadisticas = pipeline.ejecutar()
```

El resultado principal corresponde a:

* Tabla de precios promedio anuales por producto.
* Tabla de variaciones porcentuales año a año.
* Estadísticas descriptivas de `usdprice`.
* Medición de eficiencia del algoritmo recursivo.

---

## Control de versiones

El proyecto utiliza Git y GitHub para garantizar trazabilidad, reproducibilidad y trabajo colaborativo.

Ejemplos de commits asociados al desarrollo:

```text
feat: implementa estructura inicial del proyecto
feat: agrega notebook de definicion F1
feat: implementa pipeline de preprocesamiento F2
feat: exporta dataset limpio de precios europeos
feat: agrega nucleo algoritmico F3
feat: implementa clases para analisis de precios
feat: agrega algoritmo recursivo merge sort
docs: actualiza README con descripcion de Fase 3
```

---

## Limitaciones del proyecto

* El dataset no contiene información para la totalidad de los países europeos.
* La cobertura temporal y geográfica varía según país, mercado y producto.
* Los precios pueden estar influenciados por múltiples factores externos, como inflación local, costos energéticos, políticas económicas, transporte, estacionalidad y condiciones climáticas.
* El análisis permite identificar tendencias y asociaciones, pero no establece relaciones causales directas.
* El uso de precios promedio puede ocultar diferencias entre mercados, regiones o unidades de medida.
* La comparación antes y después del conflicto debe interpretarse como un análisis exploratorio, no como una prueba causal definitiva.

---

## Próximas mejoras

* Incorporar análisis mensual para observar variaciones más detalladas en torno a febrero de 2022.
* Comparar precios promedio antes y después del inicio del conflicto.
* Incorporar visualizaciones temporales por país, producto y categoría.
* Evaluar productos con mayores aumentos relativos.
* Robustecer la validación técnica mediante pruebas adicionales.
* Extender la arquitectura POO incorporando nuevas clases de análisis.
* Exportar tablas y gráficos relevantes a la carpeta `F3/results/`.

---

## Bibliografía

* McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O’Reilly Media.
* The pandas development team. (2025). *pandas documentation*. https://pandas.pydata.org/docs/
* NumPy Developers. (2025). *NumPy documentation*. https://numpy.org/doc/
* Project Jupyter. (2025). *Jupyter documentation*. https://docs.jupyter.org/
* World Food Programme. (2025). *Global Food Prices Database*. Humanitarian Data Exchange.
* Salinas, O. (2026). *Programación orientada a objetos aplicada a la ciencia de datos* [Material docente]. Universidad Andrés Bello.
* Salinas, O. (2026). *Limpieza y transformación de datos tabulares con Pandas* [Material docente]. Universidad Andrés Bello.
* Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
