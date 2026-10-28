# `datos_15.figuras/`: figuras y salidas tabulares

Las imágenes se generan con los scripts del repositorio y no llevan el título incrustado: el título y
la fuente se escriben fuera de la imagen, como piden las normas de la revista. Los nombres de archivo
conservan el orden de generación; la numeración de la tabla es la del manuscrito (Figuras 1 y 2) y la
del anexo F del material suplementario (Figuras 3 a 17), donde están los títulos y las notas.

| Figura | Archivo | Contenido | Dónde se presenta | Script |
|---:|---|---|---|---|
| 1 | `fig02_linea_doctorado.png` | Línea de doctorado de mayor interés | Manuscrito, 3.3 | `datos_11` |
| 2 | `fig13_area_x_linea.png` | Línea temática según el área disciplinaria | Manuscrito, 3.8 | `datos_12.figura-area-x-linea` |
| 3 | `fig16_mca_vista_general.png` | Análisis de correspondencias: vista general | Anexo F, 3.1 | `datos_16` |
| 4 | `fig17_mca_detalle_cumulo.png` | Análisis de correspondencias: detalle del cúmulo central | Anexo F, 3.1 | `datos_16` |
| 5 | `fig01_interes_doctorado.png` | Interés en cursar el doctorado | Anexo F, 3.2 | `datos_11` |
| 6 | `fig03_genero.png` | Género | Anexo F, 3.4 | `datos_11` |
| 7 | `fig04_edad.png` | Edad | Anexo F, 3.4 | `datos_11` |
| 8 | `fig07_area_maestria.png` | Área disciplinaria de la maestría | Anexo F, 3.4 | `datos_11` |
| 9 | `fig08_situacion_laboral.png` | Situación laboral | Anexo F, 3.4 | `datos_11` |
| 10 | `fig09_motivacion.png` | Motivación principal | Anexo F, 3.5 | `datos_11` |
| 11 | `fig10_tiempo_inicio.png` | Plazo estimado de inicio | Anexo F, 3.6 | `datos_11` |
| 12 | `fig11_situacion_x_tiempo.png` | Plazo según situación laboral (RQ6) | Anexo F, 3.7 | `datos_11` |
| 13 | `fig12_situacion_x_motivacion.png` | Motivación según situación laboral (RQ6) | Anexo F, 3.7 | `datos_11` |
| 14 | `fig05_estado_estudios.png` | Entidad donde se cursó la maestría | Anexo F, 3.9 | `datos_11` |
| 15 | `fig06_estado_residencia.png` | Lugar de residencia | Anexo F, 3.9 | `datos_11` |
| 16 | `fig14_mapa_estado_estudios.png` | Mapa por entidad de estudios | Anexo F, 3.9 | `datos_13` |
| 17 | `fig15_mapa_estado_residencia.png` | Mapa por entidad de residencia | Anexo F, 3.9 | `datos_13` |

## Salidas tabulares

| Archivo | Contenido | Script |
|---|---|---|
| `datos_15.mca-coordenadas.csv` | Coordenadas y contribuciones de las 29 categorías del análisis de correspondencias | `datos_16` |
| `datos_15.mca-dimensiones.csv` | Valores propios e inercia por dimensión | `datos_16` |
| `datos_15.mapa-estado-estudios.csv` | Personas interesadas por entidad de estudios | `datos_13` |
| `datos_15.mapa-estado-residencia.csv` | Personas interesadas por entidad de residencia | `datos_13` |

Los scripts escriben además un borrador de pies de figura (`pies-de-figura.md`) con la numeración de
generación; los títulos definitivos son los del anexo F.
