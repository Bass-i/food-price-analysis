# Impacto del conflicto Rusia-Ucrania en los precios de los alimentos en Europa (2020-2025)

## Descripción del proyecto

Este proyecto académico tiene como objetivo analizar la evolución de los precios de alimentos en Europa durante el período 2020-2025, considerando como contexto el conflicto Rusia-Ucrania y sus posibles efectos sobre los mercados alimentarios.

El análisis utiliza información proveniente de la base de datos **World Food Programme Global Food Prices Database (WFP)**. El proyecto se desarrolla progresivamente mediante las fases definidas en la asignatura **MCDI500 — Herramientas de software científico**, incorporando procesos de definición del problema, obtención de datos, limpieza, transformación, validación, análisis algorítmico, medición de eficiencia y Programación Orientada a Objetos en Python.

El desarrollo se organiza en cuatro fases principales:

* Fase 1: definición del problema, objetivos, estructura del proyecto y entorno reproducible.
* Fase 2: obtención, consolidación, limpieza, transformación y validación del dataset.
* Fase 3: construcción del núcleo algorítmico mediante programación estructurada, recursividad, medición de complejidad y Programación Orientada a Objetos.
* Fase 4: construcción de visualizaciones analíticas, interpretación de resultados y comunicación de hallazgos.

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
* Construir visualizaciones analíticas para comunicar los resultados obtenidos.
* Interpretar tendencias y patrones identificados en los datos.
* Integrar los hallazgos de las distintas fases en una comunicación analítica reproducible.

---

## Requisitos previos

Antes de ejecutar cualquier notebook, instala las dependencias del proyecto. Se recomienda usar un entorno virtual.

### Opción 1: entorno virtual (recomendado)

```bash
git clone https://github.com/Bass-i/food-price-analysis.git
cd food-price-analysis
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### Opción 2: instalación directa

```bash
git clone https://github.com/Bass-i/food-price-analysis.git
cd food-price-analysis
pip install -r requirements.txt
```

Una vez instaladas las dependencias, abre el notebook correspondiente en Jupyter y ejecuta **Kernel → Restart & Run All**.

> Los notebooks fueron desarrollados con **Python 3.12**. Se recomienda usar la misma versión para garantizar compatibilidad.

---

## Dataset

### Fuente de datos

**World Food Programme Global Food Prices Database (WFP)**
Disponible en: [Kaggle](https://www.kaggle.com/datasets/abhishekgupta56447/global-food-prices-database-wfp)

### Período analizado

2020-2025

### Archivos raw

Los archivos CSV anuales deben estar ubicados en:

```text
F1/data/raw/
├── wfp_food_prices_global_2020.csv
├── wfp_food_prices_global_2021.csv
├── wfp_food_prices_global_2022.csv
├── wfp_food_prices_global_2023.csv
├── wfp_food_prices_global_2024.csv
└── wfp_food_prices_global_2025.csv
```

El notebook de Fase 3 opera directamente desde esta carpeta. No es necesario ejecutar Fase 2 previamente.

### Variables principales

| Variable | Descripción |
|---|---|
| `countryiso3` | Código ISO del país |
| `date` | Fecha del registro |
| `admin1`, `admin2` | Regiones administrativas |
| `market` | Mercado de origen |
| `category` | Categoría del producto |
| `commodity` | Nombre del producto |
| `currency` | Moneda local |
| `unit` | Unidad de medida |
| `price` | Precio en moneda local |
| `usdprice` | Precio en dólares (variable principal) |
| `usdprice_zscore` | Precio normalizado (z-score, generado en Fase 3) |
| `archivo_origen` | Nombre del CSV de origen (trazabilidad) |

La variable principal para el análisis comparativo es `usdprice`, ya que permite comparar precios entre países utilizando una moneda común.

---

## Tecnologías utilizadas

- Python 3.12
- pandas
- NumPy
- matplotlib
- Jupyter Notebook
- Git / GitHub
- Módulos estándar: `pathlib`, `timeit`

---

## Estructura del repositorio

```text
food-price-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── F1/
│   ├── data/
│   │   └── raw/
│   │       ├── wfp_food_prices_global_2020.csv
│   │       ├── wfp_food_prices_global_2021.csv
│   │       ├── wfp_food_prices_global_2022.csv
│   │       ├── wfp_food_prices_global_2023.csv
│   │       ├── wfp_food_prices_global_2024.csv
│   │       └── wfp_food_prices_global_2025.csv
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
├──F3/
│    ├── notebooks/
│    │   └── F3_Nucleo_Algoritmico.ipynb
│    ├── src/
│    │   ├── preprocesador.py
│    │   ├── analizador.py
│    │   ├── algoritmos.py
│    │   └── pipeline.py
│    ├── docs/
│    └── results/
│        └── eficiencia_escalamiento.png
│
├── F4/
│   ├── notebooks/
│   │   └── F4_Visualizacion_Resultados.ipynb
│   ├── docs/
│   ├── results/
│   │   ├── grafico_precio_promedio.png
│   │   ├── grafico_top_aumentos.png
│   │   └── grafico_productos_seleccionados.png
│   └── src/
```

---

## Fase 1: Definición del proyecto

Durante la Fase 1 se definió la problemática central del proyecto y se estableció el entorno reproducible.

Actividades realizadas:

- Definición de la problemática y pregunta de investigación.
- Definición del objetivo general y objetivos específicos.
- Configuración del entorno de trabajo y estructura del repositorio.
- Documentación inicial en `README.md` y `requirements.txt`.

**Notebook:** `F1/notebooks/F1_Definicion.ipynb`
---

## Fase 2: Preprocesamiento y validación de datos

Durante la Fase 2 se implementó un pipeline reproducible de obtención, limpieza, transformación y validación de datos.

Actividades realizadas:

- Carga automatizada de archivos CSV anuales.
- Consolidación del dataset del período 2020-2025.
- Diagnóstico inicial, revisión de duplicados y valores faltantes.
- Conversión de `date` a formato datetime y creación de `year` y `month`.
- Filtrado de países europeos disponibles en la base WFP.
- Eliminación de registros con valores nulos en `usdprice`.
- Conservación justificada de nulos en variables geográficas no críticas.
- Validación técnica y exportación del dataset limpio.

**Notebook:** `F2/notebooks/F2_Preprocesamiento.ipynb`

**Dataset exportado:** `F2/data/processed/wfp_europe_2020_2025_clean.csv`

---

## Fase 3: Núcleo algorítmico y Programación Orientada a Objetos

La Fase 3 encapsula el pipeline completo de preprocesamiento desde los archivos raw mediante la clase `Preprocesador`, e implementa el núcleo algorítmico del proyecto con foco en diseño orientado a objetos, recursividad y eficiencia computacional.

**Notebook:** `F3/notebooks/F3_Nucleo_Algoritmico.ipynb`

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

La arquitectura se organiza en módulos con responsabilidad única:

| Archivo | Componente | Responsabilidad |
|---|---|---|
| `preprocesador.py` | `Preprocesador` | Carga archivos raw, consolida, filtra países europeos, convierte fechas, elimina nulos, normaliza `usdprice` y valida el dataset. |
| `analizador.py` | `AnalizadorBase` | Clase base abstracta que define la interfaz común `analizar()` para todos los analizadores. |
| `analizador.py` | `AnalizadorVariacionPrecios` | Calcula precios promedio anuales y variaciones porcentuales por producto. |
| `analizador.py` | `AnalizadorEstadistico` | Genera estadísticas descriptivas sobre `usdprice`. |
| `algoritmos.py` | `merge_sort` | Algoritmo recursivo de ordenamiento O(n log n). |
| `algoritmos.py` | `insertion_sort` | Segunda implementación propia O(n²) para comparación de eficiencia. |
| `pipeline.py` | `PipelineAnalisis` | Coordina el flujo completo desde carga raw hasta generación de resultados. |                             |

---

### Decisiones de diseño

**¿Por qué separar `Preprocesador` de los analizadores?**
Cada clase tiene una responsabilidad única. El `Preprocesador` transforma datos; los analizadores los interpretan. Esto reduce el acoplamiento y facilita la extensión independiente de cada componente.

**¿Por qué `AnalizadorBase` permite polimorfismo?**
Definir una interfaz común mediante `analizar()` permite ejecutar distintos analizadores con el mismo código cliente, sin conocer el tipo específico de cada uno. Esto es el principio de sustitución de Liskov aplicado en la práctica.

**¿Por qué `PipelineAnalisis` reduce acoplamiento?**
El código externo solo necesita conocer `PipelineAnalisis`. No requiere instanciar ni coordinar `Preprocesador` ni los analizadores directamente. Centraliza el flujo en un único punto de entrada.

**¿Por qué usar `merge_sort` si `sorted()` es más rápido?**
`merge_sort` tiene propósito académico: demostrar recursividad y la estrategia divide y vencerás. En producción, `sorted()` es la elección correcta por su implementación en C altamente optimizada (Timsort).

---

## Programación Orientada a Objetos en Fase 3

En esta fase se incorporan principios de Programación Orientada a Objetos para mejorar la organización, reutilización y mantenibilidad del código.

### Encapsulamiento

Los atributos internos `_df` y `_carpeta_raw` están protegidos dentro de las clases. Esto evita modificaciones accidentales desde fuera del objeto y obliga a interactuar mediante los métodos definidos.

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

## Algoritmos implementados

### merge_sort

Algoritmo recursivo de ordenamiento basado en divide y vencerás.

- **Caso base:** lista de tamaño ≤ 1.
- **Caso recursivo:** divide la lista en dos mitades y las ordena de forma recursiva.
- **Fusión:** combina los resultados parciales en orden ascendente.
- **Complejidad:** O(n log n) en todos los casos.

### insertion_sort

Algoritmo iterativo de ordenamiento por inserción, incluido como segunda implementación propia para el análisis comparativo de eficiencia.

- **Complejidad:** O(n²) promedio, O(n) mejor caso.

---

## Eficiencia y optimización

Se midió el escalamiento temporal de los tres algoritmos para tamaños de entrada n = 25, 50, 100, 200, 400, 800 y 1600, utilizando `timeit` con 200 repeticiones por tamaño.

Los resultados se presentan en una tabla comparativa y en el gráfico:

```text
F3/results/eficiencia_escalamiento.png
```

**Conclusión principal:** `merge_sort` e `insertion_sort` son implementaciones propias en Python puro. `sorted()` es más rápido en la práctica por estar implementado en C (Timsort). A medida que n crece, la diferencia entre O(n²) de `insertion_sort` y O(n log n) de `merge_sort` se vuelve visible.


## Ejecución de Fase 3

La Fase 3 encapsula el pipeline completo de preprocesamiento desde los archivos raw mediante la clase `Preprocesador`, e implementa el núcleo algorítmico del proyecto con foco en diseño orientado a objetos, recursividad y eficiencia computacional.

**Notebook:** `F3/notebooks/F3_Nucleo_Algoritmico.ipynb`

Para ejecutar el notebook de Fase 3:

```python
from pipeline import PipelineAnalisis

pipeline = PipelineAnalisis("../../F1/data/raw")
variaciones, estadisticas = pipeline.ejecutar()
```

El resultado principal corresponde a:

* Tabla de precios promedio anuales por producto.
* Tabla de variaciones porcentuales año a año.
* Estadísticas descriptivas de `usdprice`.
* Medición de eficiencia del algoritmo recursivo.

---

## Validaciones técnicas

El notebook de Fase 3 incluye validaciones formales mediante `assert`, manejo de excepciones y casos límite:

**Validaciones del dataset:**
```python
assert not df.empty
assert df.duplicated().sum() == 0
assert df["usdprice"].isna().sum() == 0
assert df["year"].between(2020, 2025).all()
assert "usdprice_zscore" in df.columns
assert "archivo_origen" in df.columns
```

**Manejo de excepciones:**
```python
try:
    Preprocesador("ruta/inexistente").cargar_archivos()
except FileNotFoundError as error:
    print(f"Excepción controlada: {error}")
```

**Casos límite de merge_sort:**
```python
assert merge_sort([]) == []
assert merge_sort([10]) == [10]
assert merge_sort([3, 2, 1]) == [1, 2, 3]
assert merge_sort([-1, 5, 0, -3]) == [-3, -1, 0, 5]
assert merge_sort([4, 2, 4, 1]) == [1, 2, 4, 4]
```

---

## Fase 4: Visualización y comunicación de resultados

La Fase 4 se enfoca en la comunicación visual de los resultados obtenidos durante las etapas anteriores. A partir del dataset preparado y validado mediante el pipeline implementado en Fase 3, se construyeron visualizaciones analíticas destinadas a identificar tendencias, variaciones y patrones relevantes en los precios de los alimentos en Europa durante el período 2020–2025.

### Objetivo de la Fase 4

Comunicar de manera clara y reproducible los principales hallazgos del proyecto mediante visualizaciones analíticas e interpretación de resultados.

### Notebook principal


F4/notebooks/F4_Visualizacion_Resultados.ipynb

## Visualizaciones implementadas

Evolución del precio promedio anual en Europa (2020–2025).
Top 10 productos con mayores aumentos porcentuales de precio.
Evolución temporal de productos seleccionados (Bread, Milk y Onions).

## Principales Hallazgos

Se observó una tendencia general de crecimiento en el precio promedio de los alimentos durante el período analizado.
Los mayores incrementos porcentuales se concentraron principalmente en productos agrícolas frescos como repollo, cebolla, zanahoria y pepino.
La evolución temporal mostró comportamientos diferenciados entre productos, evidenciando que el impacto sobre los precios no fue homogéneo.

## Resultados generados

F4/results/grafico_precio_promedio.png
F4/results/grafico_top_aumentos.png
F4/results/grafico_productos_seleccionados.png

## Ejecución de Fase 4

Para ejecutar la fase de visualización:

```python
import sys
from pathlib import Path

sys.path.append("../../F3/src")

import pandas as pd
import matplotlib.pyplot as plt

from preprocesador import Preprocesador
from analizador import AnalizadorVariacionPrecios

preprocesador = Preprocesador("../../F1/data/raw")

df = (
    preprocesador
    .cargar_archivos()
    .validar_columnas_requeridas()
    .filtrar_europa()
    .convertir_fechas()
    .eliminar_nulos_usdprice()
    .normalizar_usdprice()
    .validar()
    .obtener_dataframe()
)
```
## Notebook genera

-Gráfico de evolución anual de precios.

-Gráfico de mayores aumentos porcentuales.

-Gráfico de evolución de productos seleccionados.

-Interpretaciones analíticas.

-Conclusiones finales del proyecto.

---

## Control de versiones

El proyecto utiliza Git y GitHub para garantizar trazabilidad, reproducibilidad y trabajo colaborativo. El repositorio se organiza por fases con ramas por integrante.

Estructura de commits utilizada:

```text
feat: implementa estructura inicial del proyecto
feat: agrega notebook de definicion F1
feat: implementa pipeline de preprocesamiento F2
feat: exporta dataset limpio de precios europeos
feat: agrega nucleo algoritmico F3
feat: implementa clases para analisis de precios
feat: agrega algoritmo recursivo merge sort
feat: rehace Preprocesador para operar desde archivos raw
feat: agrega insertion_sort para comparacion de eficiencia
feat: agrega validaciones con assert y casos limite
feat: agrega grafico de escalamiento temporal
docs: actualiza README con instrucciones de reproducibilidad
feat: crea estructura inicial F4
feat: agrega visualizacion de precios promedio
feat: agrega grafico de mayores aumentos porcentuales
feat: agrega evolucion temporal de productos
feat: agrega interpretaciones y conclusiones F4
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

## Bibliografía

- McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
- The pandas development team. (2025). *pandas documentation*. Recuperado de https://pandas.pydata.org/docs/
- NumPy Developers. (2025). *NumPy documentation*. Recuperado de https://numpy.org/doc/
- Project Jupyter. (2025). *Jupyter documentation*. Recuperado de https://docs.jupyter.org/
- Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering, 9*(3), 90-95.
- World Food Programme. (2025). *Global Food Prices Database*. Humanitarian Data Exchange. Recuperado de https://data.humdata.org/dataset/wfp-food-prices
- Salinas, O. (2026). *Programación orientada a objetos aplicada a la ciencia de datos* [Material docente]. Universidad Andrés Bello.
- Salinas, O. (2026). *Limpieza y transformación de datos tabulares con Pandas* [Material docente]. Universidad Andrés Bello.
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1995). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
