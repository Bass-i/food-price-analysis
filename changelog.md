# Changelog y trazabilidad de mejoras

Este documento registra la evolución técnica del proyecto a través de las cuatro fases, vinculando explícitamente las observaciones formativas recibidas con las acciones de mejora implementadas y los commits correspondientes.

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
|---|---|---|
| 2026-06 | Corrección de la fuente de datos del notebook F4 (de CSV de F2 a Preprocesador desde raw) | Evitar la propagación del error de trazabilidad de cifras detectado en Fase 3. |
| 2026-06 | Implementación de visualización de precio promedio anual | Analizar la evolución global de los precios en Europa. |
| 2026-06 | Implementación de gráfico de mayores aumentos porcentuales | Identificar productos con mayor variación de precio, reutilizando AnalizadorVariacionPrecios de Fase 3. |
| 2026-06 | Implementación de visualización temporal de productos seleccionados | Comparar comportamientos individuales de distintos alimentos. |
| 2026-06 | Incorporación de sección de validación y reflexión técnica | Cumplir el criterio de rúbrica que exige comparación con fases previas y reflexión grupal. |
| 2026-06 | Incorporación de sección de discusión y limitaciones | Cumplir el criterio de rúbrica que exige contraste con hipótesis inicial y declaración de riesgos. |
| 2026-06 | Incorporación de sección de metodología que articula explícitamente las fases F1–F4 | Cumplir el criterio de rúbrica que exige vincular decisiones técnicas con resultados obtenidos a lo largo del proyecto. |
| 2026-06 | Corrección de filtrado en el cálculo de top_aumentos (uso de .loc en lugar de indexación booleana directa) | Eliminar advertencia de pandas (UserWarning) y garantizar alineación correcta de índices tras dropna(). |
| 2026-06 | Incorporación de interpretaciones analíticas por figura | Comunicar hallazgos de manera fundamentada. |
| 2026-06 | Incorporación de conclusiones finales | Sintetizar los resultados obtenidos durante el proyecto. |
| 2026-06 | Conversión de requirements.txt a codificación UTF-8 | Mejorar la portabilidad del entorno reproducible. |
| 2026-06 | Reestructuración de este changelog en formato tabla comparativa | Cumplir explícitamente el criterio de rúbrica "Trazabilidad de mejoras", que exige observación formativa, acción y commit verificable. |
| 2026-06 | Actualización del README y documentación técnica | Mantener coherencia entre repositorio, notebooks e informe final. |

---

## Impacto de las mejoras

Las mejoras incorporadas a lo largo de las cuatro fases permitieron evolucionar desde una definición conceptual del problema hacia una solución reproducible y modular basada en análisis de datos. La incorporación de validaciones formales, programación orientada a objetos, mediciones de eficiencia y visualizaciones analíticas fortaleció la calidad técnica, la mantenibilidad y la trazabilidad del proyecto.

Particularmente, las correcciones realizadas en Fase 4 en respuesta directa a la retroalimentación del docente sobre Fase 3 —sincronización de cifras entre informe y código, incorporación de citas APA, y prevención del mismo error de trazabilidad en el nuevo notebook— consolidan una práctica de mejora continua basada en evidencia, alineada con prácticas profesionales de desarrollo científico reproducible en Python.