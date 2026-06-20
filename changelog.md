# Changelog

## Fase 1 – Definición del proyecto

| Fecha | Cambio | Justificación técnica |
|---------|---------|---------|
| 2026-05 | Definición de la problemática y objetivos del proyecto | Establecer el alcance analítico y los objetivos de investigación. |
| 2026-05 | Configuración del entorno reproducible | Garantizar la ejecución consistente del proyecto mediante Python, Jupyter y Git. |
| 2026-05 | Creación de la estructura inicial del repositorio | Organizar el proyecto siguiendo una arquitectura por fases. |

---

## Fase 2 – Preprocesamiento y transformación de datos

| Fecha | Cambio | Justificación técnica |
|---------|---------|---------|
| 2026-05 | Consolidación de archivos CSV 2020–2025 | Integrar la información histórica en un único conjunto de datos. |
| 2026-05 | Conversión de fechas y creación de variables temporales | Facilitar análisis cronológicos mediante year y month. |
| 2026-05 | Filtrado de países europeos | Delimitar el alcance geográfico definido por el proyecto. |
| 2026-05 | Eliminación de registros con usdprice nulo | Garantizar consistencia en la variable principal de análisis. |
| 2026-05 | Exportación del dataset limpio | Generar una base reproducible para las fases posteriores. |

---

## Fase 3 – Núcleo algorítmico y Programación Orientada a Objetos

| Fecha | Cambio | Justificación técnica |
|---------|---------|---------|
| 2026-06 | Implementación de AnalizadorVariacionPrecios | Calcular precios promedio anuales y variaciones porcentuales. |
| 2026-06 | Implementación de AnalizadorEstadistico | Obtener estadísticas descriptivas de la variable usdprice. |
| 2026-06 | Implementación de merge_sort | Incorporar recursividad y análisis de complejidad algorítmica. |
| 2026-06 | Implementación de insertion_sort | Comparar distintas estrategias de ordenamiento. |
| 2026-06 | Refactorización del Preprocesador para operar desde archivos RAW | Construir un pipeline reproducible desde el origen de los datos. |
| 2026-06 | Incorporación de herencia y polimorfismo | Aplicar principios de Programación Orientada a Objetos. |
| 2026-06 | Incorporación de validaciones mediante assert | Garantizar la integridad del dataset y del procesamiento. |
| 2026-06 | Incorporación de manejo de excepciones y casos límite | Mejorar la robustez del código frente a escenarios inesperados. |
| 2026-06 | Medición de eficiencia mediante timeit | Obtener métricas reproducibles de rendimiento. |
| 2026-06 | Análisis de escalamiento algorítmico | Evaluar el comportamiento temporal frente a distintos tamaños de entrada. |

---

## Fase 4 – Visualización y comunicación de resultados

| Fecha | Cambio | Justificación técnica |
|---------|---------|---------|
| 2026-06 | Implementación de visualización de precio promedio anual | Analizar la evolución global de los precios en Europa. |
| 2026-06 | Implementación de gráfico de mayores aumentos porcentuales | Identificar productos con mayor variación de precio. |
| 2026-06 | Implementación de visualización temporal de productos seleccionados | Comparar comportamientos individuales de distintos alimentos. |
| 2026-06 | Incorporación de interpretaciones analíticas | Comunicar hallazgos de manera fundamentada. |
| 2026-06 | Incorporación de conclusiones finales | Sintetizar los resultados obtenidos durante el proyecto. |
| 2026-06 | Actualización del README y documentación técnica | Mantener coherencia entre repositorio, notebooks e informe final. |

---

## Impacto de las mejoras

Las mejoras incorporadas a lo largo de las cuatro fases permitieron evolucionar desde una definición conceptual del problema hacia una solución reproducible y modular basada en análisis de datos. La incorporación de validaciones formales, programación orientada a objetos, mediciones de eficiencia y visualizaciones analíticas fortaleció la calidad técnica, la mantenibilidad y la trazabilidad del proyecto, alineándolo con prácticas profesionales de desarrollo científico en Python.