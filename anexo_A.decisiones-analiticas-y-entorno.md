# Anexo A. Decisiones analíticas, criterios de estructura curricular y entorno de cómputo

**Se cita en:** apartados 2.6, 2.7 y 4.2 del manuscrito.
**Fuentes:** `datos_17.reporte-cifras-canonicas.R` y su salida, y `datos_18.sensibilidad-rq7.R`.

## A.1 Plan de análisis

Las ocho preguntas de investigación se definieron antes de programar cualquier cálculo (apartado 1.5). Los apartados 3.2 a 3.9 les responden en ese orden. El análisis de correspondencias múltiples del apartado 3.1 es exploratorio y no responde a ninguna pregunta.

| Pregunta | Qué examina | Base | Procedimiento | Apartado | Resultado |
|---|---|---:|---|---|---|
| RQ1 | Proporción con interés | 113 | Proporción e intervalo exacto de Clopper-Pearson | 3.2 | 88.5 % [81.1, 93.7] |
| RQ2 | Línea temática preferida | 100 | Frecuencias | 3.3 | 55.0 % manejo y aprovechamiento |
| RQ3 | Perfil de las personas interesadas | 100 | Frecuencias; asociación del interés con género y edad sobre 113 | 3.4 | Sin asociación con género ni con edad |
| RQ4 | Motivación principal | 100 | Frecuencias | 3.5 | 53.0 % investigación |
| RQ5 | Plazo de inicio | 100 | Frecuencias | 3.6 | 72.0 % en dos años o menos |
| RQ6 | Situación laboral × plazo y × motivación | 98 | Fisher con simulación Monte Carlo; V de Cramér | 3.7 | p = 0.289 y 0.079; V = 0.211 y 0.240 |
| RQ7 | Área disciplinaria × línea | 100 | Fisher con simulación Monte Carlo; V de Cramér; sensibilidad | 3.8 | p = 0.034; V = 0.417; sin las áreas de menos de cinco casos, p = 0.202 |
| RQ8 | Entidad de estudios × residencia | 100 | Proporción e intervalo exacto; Fisher con simulación; V de Cramér | 3.9 | 82.0 % [73.1, 89.0]; V = 0.890 |

## A.2 Bases de cálculo

| Base | n | Se usa en |
|---|---:|---|
| Todas las respuestas | 113 | RQ1 y la asociación del interés con género y edad |
| Personas interesadas | 100 | Línea, motivación, plazo, perfil, RQ7 y RQ8 |
| Interesadas con dato de situación laboral | 98 | RQ6 y el análisis de correspondencias múltiples |

Las 13 personas sin interés también respondieron motivación y plazo; esas respuestas se excluyen porque no describen a quienes cursarían el programa. Con ellas incluidas, ninguna proporción de esos dos reactivos cambia más de 3.2 puntos porcentuales (apartado 2.5).

## A.3 Las cuatro decisiones analíticas

| Decisión | Regla | Justificación | Implicación de lectura |
|---|---|---|---|
| 1. Prueba de asociación | Si más del 20 % de las frecuencias esperadas es menor que cinco (regla de Cochran), se usa la prueba exacta de Fisher; en tablas mayores que 2 × 2, con simulación Monte Carlo: 200 000 réplicas (RQ6 y RQ7) y 50 000 (RQ8), con una semilla por prueba (20260727 a 20260730) | Las cuatro tablas superan el umbral: 76.0 %, 55.0 %, 87.5 % y 100.0 % de frecuencias esperadas menores que cinco | El error de simulación es cercano a 0.001: las diferencias en el tercer decimal no se interpretan. La sensibilidad de RQ7 usa la semilla 20260731 |
| 2. Tamaño del efecto | V de Cramér en todo cruce, con o sin significancia | Con n = 98 a 100, una asociación real puede no alcanzar el umbral convencional | RQ6b (p = 0.079; V = 0.240) se lee como «no se detectó asociación con esta muestra», no como «no hay asociación» |
| 3. Tendencia por edad | Regresión logística sobre el límite inferior de cada rango, contrastada con el coeficiente de Spearman | Los dos procedimientos tienen supuestos distintos: tendencia lineal en la escala logit, frente a relación monótona | β = −0.0373 por año (razón de momios por cinco años = 0.830; z = −1.415; p = 0.157); ρ = −0.047 (p = 0.623). No hay tendencia sistemática |
| 4. Análisis de correspondencias múltiples | Seis variables, 98 casos completos, sin imputación | Ofrece un panorama del conjunto antes de las pruebas pareadas | Los dos ejes explican el 17.41 %: es exploratorio (anexo C) |

Proporción de personas interesadas por rango de edad, sobre las 113 respuestas: 21 a 25: 75.0 % (n = 8) · 26 a 30: 89.5 % (n = 38) · 31 a 35: 95.8 % (n = 24) · 36 a 40: 100.0 % (n = 12) · 41 a 45: 85.7 % (n = 7) · 46 a 50: 100.0 % (n = 7) · 51 a 55: 72.7 % (n = 11) · 56 a 60: 100.0 % (n = 4) · 61 o más: 0.0 % (n = 2).

## A.4 Criterios de estructura curricular

Los tres criterios del apartado 4.2 se desprenden de resultados concretos:

| Criterio | Resultado que lo sustenta | Implicación para el plan de estudios |
|---|---|---|
| 1. Situar la formación metodológica en los primeros semestres | Cohorte de composición mixta: 49.0 % de áreas sociales, 28.0 % agronómicas y 18.0 % de otras áreas | Un piso metodológico común antes de especializarse, coherente con la fase teórico-metodológica (semestres 1 y 2) de la propuesta curricular |
| 2. Conservar la vinculación territorial como actividad académica, no optativa | El 16.0 % declaró la aplicación en campo como motivación principal: una de cada seis personas | La vinculación con el territorio forma parte del plan, no de un complemento optativo |
| 3. Orientar los proyectos de investigación hacia problemas del territorio de procedencia | El 82.0 % reside donde cursó su maestría y las personas interesadas proceden de 17 entidades | Con un programa presencial en sede única, el trabajo de campo puede situarse donde el problema existe (apartado 4.4) |

## A.5 Entorno de cómputo

| Corrida | Software | Sistema | Uso |
|---|---|---|---|
| Canónica (27 de julio de 2026) | R 4.5.3 con RStudio 2026.06.0+242; stringi 1.8.7, openxlsx 4.2.8.1, writexl 1.5.4, dplyr 1.2.1, stringr 1.6.0, readxl 1.5.0 | Fedora Linux 43 | Cifras canónicas (anexo G); la sesión completa está al final de `datos_17.reporte-cifras-canonicas.txt` |
| Réplica de verificación (27 de octubre de 2026) | R 4.3.3; ggplot2 3.4.4, ggrepel 0.9.5, FactoMineR 2.9, sf 1.0.15, scales 1.3.0, dplyr 1.1.4 | Ubuntu 24.04.5 | Limpieza, cifras, sensibilidad, análisis de correspondencias y las diecisiete figuras |
| Verificación independiente (27 de octubre de 2026) | Python 3.13; numpy 2.5.3, pandas 3.0.5, scipy 1.18.1 | Ubuntu 24.04.5 | Recálculo de todas las cifras con otro algoritmo de simulación (anexo G) |

**Orden de ejecución:** `datos_03` (limpieza) → `datos_10` (verificación de la limpieza) → `datos_11` y `datos_12` (análisis descriptivo y Figura 2) → `datos_13` (mapas) → `datos_16` (análisis de correspondencias) → `datos_17` (cifras canónicas) → `datos_18` (sensibilidad de RQ7) → `datos_19` (verificación en Python).

---

*Versión para arbitraje ciego.* Las personas autoras y la institución sede se designan como Autor/a, y las instituciones del anexo B con un código. Los nombres se restituyen en la versión definitiva, tras la aceptación del artículo.
