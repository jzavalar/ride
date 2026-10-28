# Anexo C. Análisis de correspondencias múltiples

**Se cita en:** apartado 3.1 del manuscrito (especificación en el apartado 2.6).
**Script:** `datos_16.mca-exploratorio.R`. **Salidas:** `datos_15.mca-dimensiones.csv` y `datos_15.mca-coordenadas.csv`. **Figuras:** 3 y 4 de este material (anexo F).

## C.1 Qué es y qué no es

El análisis de correspondencias múltiples proyecta en un mismo plano las categorías de varias variables cualitativas: la proximidad entre dos categorías sugiere que tienden a presentarse en los mismos casos. En este estudio es un panorama exploratorio, previo a las preguntas de investigación. No sustituye las pruebas de RQ6 y RQ7 y no se le atribuye ningún valor p.

## C.2 Especificación

| Elemento | Valor |
|---|---|
| Variables activas | Seis: género, edad, área de la maestría, situación laboral, motivación y plazo de inicio |
| Casos | 98 personas interesadas con dato completo en las seis variables (se excluyen las 2 sin dato de situación laboral; no se imputa) |
| Categorías proyectadas | 29: Edad (8), Área de maestría (5), Situación laboral (5), Tiempo de inicio (5), Motivación (4), Género (2) |
| Implementación | `FactoMineR::MCA`, R |

## C.3 Inercia explicada

| Dimensión | Valor propio | % de inercia | % acumulado |
|---|---:|---:|---:|
| Dimensión 1 | 0.364 | 9.49 | 9.49 |
| Dimensión 2 | 0.303 | 7.92 | 17.41 |

Los dos ejes retienen el 17.41 % de la inercia total, menos de una quinta parte. Por eso el mapa se lee como panorama y no como estructura confirmada (apartado 3.1 y séptima limitación del apartado 4.6). La verificación en Python del anexo G reproduce los dos valores propios y la inercia.

## C.4 Categorías que más contribuyen a los ejes

| Categoría | Variable | Casos | Contribución total (%) | Coordenadas (eje 1, eje 2) |
|---|---|---:|---:|---|
| Aplicación en campo | Motivación | 16 | 20.17 | 0.55, 1.41 |
| En 2 años | Tiempo de inicio | 17 | 15.91 | −0.15, 1.28 |
| Indefinido | Tiempo de inicio | 17 | 15.60 | 1.40, −0.12 |
| Otras | Área de maestría | 18 | 13.59 | 1.27, −0.01 |
| 46 a 50 | Edad | 7 | 11.47 | 0.38, −1.67 |
| Alimentos | Área de maestría | 2 | 10.69 | 0.35, −3.07 |
| Docente | Situación laboral | 21 | 10.13 | 0.45, −0.83 |
| En 3 años | Tiempo de inicio | 9 | 10.01 | −0.76, −1.23 |

Ninguna de las ocho es la categoría más frecuente de su variable. Las categorías modales (Femenino, 26 a 30, Social, Solo estudia, Investigación, En 1 año) se sitúan en el cúmulo central. Es el comportamiento característico de la técnica: las categorías minoritarias se alejan del centro y pesan más en la formación de los ejes, sin que eso las haga más importantes.

## C.5 Lectura de las figuras

**Figura 3 (vista general).** Muestra las 29 categorías. Las de menor frecuencia ocupan la periferia; el área sombreada marca la región ampliada en la Figura 4.

**Figura 4 (detalle del cúmulo central).** Amplía las 15 categorías que se superponen en la vista general: 26 a 30, 31 a 35, 41 a 45, Agronómica, Docencia, Docente, Empleado, En 1 año, Femenino, Investigación, Masculino, Negocio propio, Social, Solo estudia, Trabaja y estudia.

## C.6 Interpretación

Las categorías más frecuentes de las seis variables se agrupan en la región central del plano y no se aprecian subgrupos diferenciados: el conjunto de personas interesadas es relativamente homogéneo en su perfil de demanda (apartado 3.1). Esta lectura es coherente con los resultados de las pruebas de asociación, pero no los sustituye: RQ6 no mostró asociación significativa y la asociación de RQ7 se interpreta como indicio exploratorio (apartados 3.7 y 3.8).

---

*Versión para arbitraje ciego.* Las personas autoras y la institución sede se designan como Autor/a, y las instituciones del anexo B con un código. Los nombres se restituyen en la versión definitiva, tras la aceptación del artículo.
