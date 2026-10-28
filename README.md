# Material suplementario

**Artículo:** *Demanda de un Doctorado en Ciencias en Manejo y Aprovechamiento del Paisaje Rural integrado a una maestría profesionalizante.*

Estos materiales se citan en el manuscrito como Autor/a (s.f.). No son material accesorio: la declaración de reproducibilidad del apartado 2.7 depende de ellos.

Los anexos, el instrumento y el diccionario están reunidos en `material-suplementario_anexos-A-H.pdf` (también en `.docx`); cada anexo está además en Markdown, con sus figuras y tablas.

## Anexos

| Anexo | Archivo | Contenido | Se cita en |
|---|---|---|---|
| A | `anexo_A.decisiones-analiticas-y-entorno.md` | Plan de análisis, bases de cálculo, las cuatro decisiones analíticas, criterios de estructura curricular y entorno de cómputo | 2.6, 2.7 y 4.2 |
| B | `anexo_B.programas-de-maestria-declarados.md` | Programas de maestría declarados, con institución codificada y entidad | 2.2 |
| C | `anexo_C.analisis-correspondencias-multiples.md` | Especificación, inercia, contribuciones e interpretación de las Figuras 3 y 4 | 3.1 |
| D | `anexo_D.perfil-de-egreso.md` | Perfil de egreso completo y su correspondencia con los resultados | 4.3 |
| E | `anexo_E.catalogo-area-disciplinaria.md` | Correspondencia entre cada nombre de maestría y su área disciplinaria | 2.3 |
| F | `anexo_F.figuras-complementarias.md` | Figuras 3 a 17, con la correspondencia entre archivo y número | 3.1 y 3.9 |
| G | `anexo_G.reporte-canonico-y-verificacion.md` | Cifras canónicas, reproducción, verificación en Python y sensibilidad de RQ7 | 2.6 y 2.7 |
| H | `anexo_H.fuentes-tabla-1.md` | Fuentes, fechas de consulta y conversión de costos de la Tabla 1 | 1.4 |

## Instrumento, datos y scripts

El apartado 2.7 del manuscrito pone a disposición los datos brutos y limpios, el catálogo de estandarización de entidades, el diccionario de datos, los scripts de limpieza, análisis y graficación y la réplica del entorno de ejecución. Están en la carpeta `repositorio/`, en la disposición en que se ejecutan; su `README.md` indica el orden. Para leerlos sin abrir los archivos, `datos_instrumento-y-diccionario.md` reproduce el instrumento y las variables del diccionario.

| Material | Archivos en `repositorio/` |
|---|---|
| Instrumento de levantamiento | `datos_00` (.docx y .md) |
| Datos brutos | `datos_01` (.xlsx y .csv), 113 respuestas |
| Catálogo de estandarización de entidades | `datos_02` |
| Datos limpios | `datos_04` (113 respuestas) y `datos_05` (100 personas interesadas), en .csv, .xlsx y .rds |
| Diccionario de datos | `datos_06` (.xlsx) |
| Scripts de limpieza, análisis y graficación | `datos_03`, `datos_10` a `datos_13` y `datos_16` a `datos_19` |
| Réplica del entorno de ejecución | `datos_08` (sesión de R de la corrida canónica) y `datos_09` (instaladores e instrucciones) |
| Documentación y salidas | `README.md`, `LICENSE.txt`, `datos_07` (validación de la limpieza), `datos_14` (tablas de resultados) y `datos_15.figuras/` |

En esta versión para arbitraje, la institución de procedencia aparece con el código del anexo B; el resto de los datos es el original. La versión anonimizada reproduce las mismas cifras, tablas y figuras (anexo G).

**Carpetas:** `figuras/` (diecisiete imágenes PNG de 300 ppp), `tablas/` (anexos B y E en CSV), `verificacion/` (scripts y salidas de los anexos A y G) y `repositorio/` (instrumento, datos, diccionario y scripts).

---

*Versión para arbitraje ciego.* Las personas autoras y la institución sede se designan como Autor/a, y las instituciones del anexo B con un código. Los nombres se restituyen en la versión definitiva, tras la aceptación del artículo.

## Licencia

Creative Commons Atribución 4.0 Internacional (CC BY 4.0). El texto legal completo está en `LICENSE.txt`; resumen en español: https://creativecommons.org/licenses/by/4.0/deed.es

Los datos, el instrumento de levantamiento, los scripts y su documentación pueden copiarse, redistribuirse, adaptarse y usarse para cualquier fin, incluso comercial, siempre que se otorgue el crédito correspondiente, se indique si se realizaron cambios y se enlace a la licencia.

**Cómo citar (versión para arbitraje ciego):**
Autor/a. (s.f.). Repositorio de datos y materiales complementarios [Conjunto de datos].
