# Changelog y trazabilidad de mejoras

Este documento registra la evolución técnica del proyecto a través de las cuatro fases, vinculando explícitamente las observaciones formativas recibidas con las acciones de mejora implementadas y los commits correspondientes.

## Registro cronológico por fase

### Fase 1 — Definición del proyecto

| Fecha | Autor | Commit | Cambio |
|---|---|---|---|
| 2026-06-02 | Bass_i (Renato) | `6d28543` | Inicializa estructura del proyecto |
| 2026-06-02 | Bass_i (Renato) | `ebcb7ba` | Agrega documentacion inicial del proyecto |
| 2026-06-02 | Bass_i (Renato) | `4ca054f` | Implementa notebook F1 definicion |
| 2026-06-03 | Bass_i (Renato) | `d574dc5` | Actualiza dependencias para entorno reproducible |
| 2026-06-07 | Fabian Castillo | `8af3350` | Se actualiza README especificando cada apartado. Se agregan más topicos como #control de versiones, #objetivos especificos, #limitaciones iniciales, etc. |
| 2026-06-08 | Fabián Castillo Rojas | `0d9f8fa` | Se crean las funciones basicas como lectura de los archivos csv, resumen del dataset, revision de valores nulos y tipos de datos |

---

### Fase 2 — Preprocesamiento y transformación de datos

| Fecha | Autor | Commit | Cambio |
|---|---|---|---|
| 2026-06-09 | Bass_i (Renato) | `39b71a0` | Implementa pipeline de limpieza, transformacion y validacion F2 |
| 2026-06-09 | Fabian Castillo | `bb29cf4` | se modifica agrega funcion de revisar los tipos de datos |
| 2026-06-10 | Fabian Castillo | `a4a550d` | se adicionan mas funciones correspondientes al tratamiento del dataset |
| 2026-06-10 | Bass_i (Renato) | `7a826b9` | Actualiza README con avances y estructura de F2 |

---

### Fase 3 — Núcleo algorítmico y Programación Orientada a Objetos

| Fecha | Autor | Commit | Cambio |
|---|---|---|---|
| 2026-06-11 | Bass_i (Renato) | `a160a2c` | feat: inicializa estructura modular de F3 |
| 2026-06-11 | Bass_i (Renato) | `55d9ec0` | feat: implementa nucleo algoritmico y analisis de eficiencia en F3 |
| 2026-06-11 | Bass_i (Renato) | `9f726cf` | feat: incorpora herencia y polimorfismo al nucleo algoritmico F3 |
| 2026-06-11 | Bass_i (Renato) | `484b9ba` | feat: implementa pipeline de analisis orientado a objetos |
| 2026-06-11 | Bass_i (Renato) | `f04ba5a` | feat: completa nucleo algoritmico, recursividad y poo en F3 |
| 2026-06-13 | Fabian Castillo | `0967862` | docs: actualiza README con descripción de Fase 3 |
| 2026-06-15 | Bass_i (Renato) | `a352b57` | feat: agrega validaciones reproducibles y manejo de excepciones en F3 |
| 2026-06-17 | Bass_i (Renato) | `a38b5a6` | feat: reconstruye pipeline desde datos raw y encapsula transformaciones |
| 2026-06-17 | Bass_i (Renato) | `599f9c9` | feat: agrega validaciones y analisis de escalamiento F3 |
| 2026-06-18 | Fabian Castillo Rojas | `9dafc33` | feat: se reemplaza funcion cargar_archivos para que tome la carpeta de los archivos raw en vez de declararlos manualmente |
| 2026-06-18 | Fabian Castillo Rojas | `503f40e` | feat: se crea nueva funcion que valida si las columnas necesarias para el análisis estan en el dataframe |
| 2026-06-18 | Fabian Castillo Rojas | `ba8e404` | feat: se retoca la funcion filtrar_europa para determinar la cantidad de filas filtradas y las que quedan |
| 2026-06-18 | Fabian Castillo Rojas | `dfb2fc0` | feat: se crea funcion normalizar_usdprice para comparacion de precios de distinta scala |
| 2026-06-18 | Fabian Castillo Rojas | `ebed682` | feat: se agrega control para determinar si existe o no un df para retornar |
| 2026-06-18 | Fabian Castillo Rojas | `875927c` | feat: se modifica codigo de pipeline.py en donde se corrige la lectura de un archivo único en vez de la carpeta con los archivos raw |
| 2026-06-18 | Fabian Castillo Rojas | `8aefb3c` | feat y doc: Se agrega docstring de los algoritmos merge_sort y fusionar. Adicionalmente se agrega la funcion insertion_sort para hacer la comparativa con merge_sort |
| 2026-06-18 | Fabian Castillo Rojas | `f55f1d1` | doc: se agrega docstring a las clases y funciones dentro del archivo analizador.py |
| 2026-06-18 | Fabian Castillo Rojas | `dfdea9e` | docs: se agregaron docstring de secciones de pipeline de analisis y aplicacion de herencia y polimorfismo. Se agrega justificación de arquitectura. |
| 2026-06-18 | Fabian Castillo Rojas | `6249628` | docs: se agrega docstring de la justificacion de aquitectura |

---

### Fase 4 — Visualización y comunicación de resultados

| Fecha | Autor | Commit | Cambio |
|---|---|---|---|
| 2026-06-19 | Bass_i (Renato) | `b56f9d7` | feat: implementa visualizaciones e interpretacion de resultados F4 |
| 2026-06-19 | Bass_i (Renato) | `3ec817b` | feat: Actualizacion documentacion f4 |
| 2026-06-20 | Bass_i (Renato) | `3ec495c` | docs: agrega changelog de evolucion tecnica F1-F4 |
| 2026-06-21 | Fabian Castillo Rojas | `dbda922` | feat: se agregan visuales a graficos para mejor interpretacion. |
| 2026-06-21 | Fabian Castillo Rojas | `b74f85b` | feat: se crea apartado de metodología de desarrollo tecnico |
| 2026-06-21 | Fabian Castillo Rojas | `7c4e0b9` | feat: se corrige warning del segundo gráfico |
| 2026-06-21 | Fabian Castillo Rojas | `af1c6e1` | Se modifica changelog angregando más commits realizados |
| 2026-06-21 | Fabian Castillo Rojas | `b47772e` | feat: convierte requirements.txt a UTF-8 segun observacion |
| 2026-06-21 | Fabian Castillo Rojas | `51d0e91` | feat: se corrige parte de las conclusiones |
| 2026-06-21 | Fabian Castillo Rojas | `e1a1bcf` | docs: se corrige en README.md la lectura de la data a procesar en la fase 4 |
| 2026-06-21 | Fabian Castillo Rojas | `4cbd88d` | docs: actualizacion README.md para eliminar a un integrante |

---

## Impacto de las mejoras

Las mejoras incorporadas a lo largo de las cuatro fases permitieron evolucionar desde una definición conceptual del problema hacia una solución reproducible y modular basada en análisis de datos. La incorporación de validaciones formales, programación orientada a objetos, mediciones de eficiencia y visualizaciones analíticas fortaleció la calidad técnica, la mantenibilidad y la trazabilidad del proyecto.

Particularmente, las correcciones realizadas en Fase 4 en respuesta directa a la retroalimentación del docente sobre Fase 3 —sincronización de cifras entre informe y código, migración de AnalizadorBase a una clase abstracta real, incorporación de citas APA, y prevención del mismo error de trazabilidad en el nuevo notebook— consolidan una práctica de mejora continua basada en evidencia, alineada con prácticas profesionales de desarrollo científico reproducible en Python.

Durante esta fase el equipo de trabajo se redujo de tres a dos integrantes. Toda la documentación del proyecto (portada, README, notebooks) fue actualizada para reflejar la composición final del equipo, y este changelog mantiene la observación original del docente sobre trazabilidad de commits como registro histórico, contextualizada con la causa real del hallazgo.

> **Nota de mantenimiento:** todos los hashes de commit listados en este documento son verificables directamente en el historial del repositorio mediante `git show <hash>` o desde la interfaz de GitHub.