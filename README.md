# Impacto del conflicto Rusia-Ucrania en los precios de los alimentos en Europa (2020-2025)

## Descripción del proyecto

Este proyecto tiene como objetivo analizar la evolución de los precios de alimentos en Europa durante el período 2020-2025, considerando como contexto el conflicto Rusia-Ucrania y sus posibles efectos sobre los mercados alimentarios.

El análisis utiliza información proveniente de la base de datos **World Food Programme Global Food Prices Database (WFP)**. El proyecto se desarrolla progresivamente mediante las fases definidas en la asignatura, incorporando procesos de obtención, limpieza, transformación, validación y análisis de datos utilizando herramientas del ecosistema científico de Python.

Actualmente el repositorio contiene el desarrollo de las fases F1 y F2 del proyecto.

---

## Objetivo general

Analizar la evolución de los precios de alimentos en países europeos disponibles dentro del conjunto de datos del WFP durante el período 2020-2025, con el fin de identificar tendencias y posibles efectos asociados al contexto del conflicto Rusia-Ucrania.

---

## Objetivos específicos

* Configurar un entorno reproducible utilizando Python, Git, GitHub y Jupyter Notebook.
* Consolidar los archivos de datos correspondientes al período 2020-2025.
* Realizar procesos de limpieza y validación del conjunto de datos.
* Transformar variables relevantes para análisis temporal.
* Filtrar los países europeos disponibles dentro de la cobertura del WFP.
* Generar un dataset procesado para las siguientes fases de análisis exploratorio y evaluación de resultados.

---

## Dataset

**Fuente de datos:**

World Food Programme Global Food Prices Database (WFP)

**Período analizado:**

2020-2025

**Variables principales:**

* País (`countryiso3`)
* Fecha (`date`)
* Mercado (`market`)
* Categoría (`category`)
* Producto (`commodity`)
* Precio local (`price`)
* Precio en USD (`usdprice`)

---

## Tecnologías utilizadas

* Python 3.12
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* Git
* GitHub

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
│   ├── notebooks/
│   ├── docs/
│   └── results/
│
└── F2/
    ├── data/
    │   └── processed/
    ├── notebooks/
    │   └── F2_Preprocesamiento.ipynb
    ├── docs/
    ├── results/
    └── src/
```

---

## Fase 1: Definición del proyecto

Durante esta fase se definió la problemática, el alcance, los objetivos y la estructura técnica del proyecto. Además, se configuró el entorno reproducible mediante Git, GitHub, Jupyter Notebook y gestión de dependencias.

**Notebook principal:**

* `F1/notebooks/F1_Definicion.ipynb`

---

## Fase 2: Preprocesamiento y validación de datos

Durante esta fase se implementó un pipeline reproducible de procesamiento de datos que incluye:

* Carga automatizada de archivos CSV.
* Consolidación de datos 2020-2025.
* Revisión de calidad de datos.
* Detección de valores faltantes.
* Conversión de fechas.
* Creación de variables temporales.
* Filtrado de países europeos.
* Limpieza de registros con valores faltantes críticos.
* Validación del dataset resultante.
* Exportación de una versión procesada del conjunto de datos.

**Notebook principal:**

* `F2/notebooks/F2_Preprocesamiento.ipynb`

**Dataset generado:**

* `F2/data/processed/wfp_europe_2020_2025_clean.csv`

---

## Reproducibilidad

### Crear entorno virtual

```bash
python -m venv .venv
```

### Activar entorno

Windows:

```bash
.venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar notebooks

Abrir Jupyter Notebook o PyCharm y ejecutar los notebooks correspondientes a cada fase.

---

## Control de versiones

El proyecto utiliza Git y GitHub para garantizar trazabilidad y reproducibilidad.

Ejemplos de commits realizados durante el desarrollo:

* Inicializa estructura del proyecto.
* Implementa notebook F1 definición.
* Actualiza dependencias para entorno reproducible.
* Implementa pipeline de preprocesamiento y validación F2.

---

## Limitaciones actuales

* El dataset no contiene información para la totalidad de los países europeos.
* La cobertura temporal y geográfica varía según el país.
* Existen factores externos que pueden influir en los precios observados, tales como inflación local, políticas económicas, costos energéticos y condiciones climáticas.
* Los resultados obtenidos permitirán identificar asociaciones y tendencias, pero no establecer relaciones causales directas.

