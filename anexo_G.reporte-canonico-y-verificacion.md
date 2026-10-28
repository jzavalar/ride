# Anexo G. Reporte canónico de cifras, verificación en dos lenguajes y sensibilidad de RQ7

**Se cita en:** apartados 2.6 y 2.7 del manuscrito.
**Archivos:** carpeta `verificacion/`: reporte canónico (`datos_17`), sensibilidad de RQ7 (`datos_18`) y verificación independiente en Python (`datos_19`), con sus salidas.

## G.1 Cifras canónicas

Todas las cifras del manuscrito proceden de una corrida única de `datos_17.reporte-cifras-canonicas.R` con semilla fija (R 4.5.3, Fedora Linux 43; anexo A). El reporte completo está en `verificacion/datos_17.reporte-cifras-canonicas.txt`, y la réplica de esta versión, en `verificacion/datos_17.reporte-cifras-canonicas.replica-20261027.txt`. Los rótulos del reporte canónico son los de la versión del script que se distribuye; sus cifras y la sesión de R son las de la corrida canónica, y la réplica las reproduce.

| Indicador | Base | Valor | Apartado |
|---|---:|---|---|
| Interés en cursar el doctorado | 113 | 100 (88.5 %; IC 95 %: 81.1 % a 93.7 %) | 3.2 |
| Manejo y aprovechamiento del paisaje rural | 100 | 55.0 % | 3.3 |
| Desarrollo del paisaje rural / paisaje y turismo rural | 100 | 17.0 % / 17.0 % | 3.3 |
| Motivación: investigación / docencia / aplicación en campo | 100 | 53.0 % / 30.0 % / 16.0 % | 3.5 |
| Inicio en un año / en dos años o menos | 100 | 55.0 % / 72.0 % | 3.6 |
| RQ6a: situación laboral × plazo | 98 | p = 0.2894; V = 0.2105 | 3.7 |
| RQ6b: situación laboral × motivación | 98 | p = 0.0788; V = 0.2403 | 3.7 |
| RQ7: área disciplinaria × línea | 100 | p = 0.0341; V = 0.4168 | 3.8 |
| Permanencia en la entidad de estudios | 100 | 82 (82.0 %; IC 95 %: 73.1 % a 89.0 %) | 3.9 |
| RQ8: entidad de estudios × residencia | 100 | p < 0.001; V = 0.8900 | 3.9 |

## G.2 Reproducción de esta versión

El 27 de octubre de 2026 se volvió a ejecutar el procedimiento completo desde los datos brutos, en R 4.3.3 sobre Ubuntu 24.04.5:

| Comprobación | Resultado |
|---|---|
| La limpieza (`datos_03`) reproduce los datos limpios | `datos_04` y `datos_05` idénticos byte a byte (MD5 a229708063f6… y 239154cf3da3…) |
| El reporte canónico (`datos_17`) reproduce todas las cifras | Idénticas, incluidos los valores p simulados, que dependen solo de la semilla de cada prueba |
| Las figuras del manuscrito se regeneran sin cambios | Figuras 1 y 2 idénticas byte a byte a las incrustadas en el artículo |
| Los datos con la institución codificada (carpeta `repositorio/`) reproducen el análisis | `datos_03` regenera sus `datos_04` y `datos_05` byte a byte (MD5 1c5cb5a396be… y 140db77219e8…); las tablas de `datos_14` y las diecisiete figuras son idénticas, y los valores p de `datos_14` coinciden con el reporte canónico |

## G.3 Verificación independiente en Python

`datos_19.verificacion-independiente.py` recalcula las cifras sin reutilizar el código de R. Para los valores p usa otro algoritmo de simulación: permuta las etiquetas de una variable, en lugar de generar tablas aleatorias con márgenes fijos como hace R. Las cifras deterministas coinciden dígito por dígito; los valores p simulados difieren dentro del error de simulación.

| Cifra | R (`datos_17`, `datos_18`) | Python (`datos_19`) |
|---|---|---|
| Interés: IC 95 % (Clopper-Pearson) | [81.13, 93.73] | [81.13, 93.73] |
| Permanencia: IC 95 % | [73.05, 88.97] | [73.05, 88.97] |
| Género × interés: p de Fisher | 0.7705 | 0.7705 |
| Edad: β por año / p | −0.03727 / 0.1571 | −0.03727 / 0.1571 |
| Edad: ρ de Spearman / p | −0.0467 / 0.6234 | −0.0467 / 0.6234 |
| RQ6a: p / V | 0.2894 / 0.2105 | 0.2902 (ee 0.0010) / 0.2105 |
| RQ6b: p / V | 0.0788 / 0.2403 | 0.0773 (ee 0.0006) / 0.2403 |
| RQ7: p / V | 0.0341 / 0.4168 | 0.0347 (ee 0.0004) / 0.4168 |
| RQ7 sin áreas de menos de cinco casos: p / V | 0.2021 / 0.3003 | 0.2035 (ee 0.0009) / 0.3003 |
| RQ8: p / V | < 0.001 / 0.8900 | < 0.001 / 0.8900 |
| Análisis de correspondencias: inercia de dos ejes | 17.41 % | 17.41 % |

## G.4 Sensibilidad de RQ7

La asociación de RQ7 depende de las dos áreas con menos de cinco casos: el área económica (tres personas, ninguna eligió manejo y aprovechamiento) y la de alimentos (dos personas, ambas lo eligieron). Se repitió la prueba sin ellas, con el mismo procedimiento y semilla propia:

| Variante | Tabla | n | p | V de Cramér | Semilla |
|---|---|---:|---:|---:|---|
| Canónica: cinco áreas × ocho líneas | 5 × 8 | 100 | 0.0341 | 0.4168 | 20260729 |
| Sin las dos áreas de menos de cinco casos | 3 × 7 | 95 | 0.2021 | 0.3003 | 20260731 |
| Ídem, con las líneas de respuesta libre agrupadas en «otra» | 3 × 4 | 95 | 0.3922 | 0.1846 | 20260732 |

En las tres áreas con más casos, la proporción que elige manejo y aprovechamiento es semejante: social, 57.1 %; agronómica, 53.6 %; otras, 55.6 %. Por eso el manuscrito interpreta la asociación como indicio exploratorio (apartado 3.8).

---

*Versión para arbitraje ciego.* Las personas autoras y la institución sede se designan como Autor/a, y las instituciones del anexo B con un código. Los nombres se restituyen en la versión definitiva, tras la aceptación del artículo.
