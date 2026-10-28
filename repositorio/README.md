# Repositorio de datos y materiales complementarios

Datos, instrumento, diccionario y scripts del artículo «Demanda de un Doctorado en Ciencias en Manejo y Aprovechamiento del Paisaje Rural integrado a una maestría profesionalizante». En el manuscrito se cita como
Autor/a (s.f.).

## Versión para arbitraje ciego

- Las personas autoras y la institución sede se designan como Autor/a.
- En los archivos de datos, la institución donde cada persona cursó la maestría
  (`universidad_estudios_maestria`) aparece con un código, de I01 a I20, el mismo del anexo B del
  material suplementario. El resto de los valores no se modificó.
- Los nombres se restituyen en la versión definitiva, que tendrá identificador permanente.

## Contenido

| Archivo | Contenido |
|---|---|
| `datos_00.instrumento-cuestionario.docx` y `.md` | Instrumento de levantamiento: diez reactivos; el `.md` es una transcripción con una nota sobre la pregunta filtro del formulario en línea |
| `datos_01.datos-brutos-cuestionario.xlsx` y `.csv` | Datos brutos: las 113 respuestas tal como se exportaron del formulario en línea; la limpieza lee el `.xlsx` |
| `datos_02.catalogo-estandarizacion-entidades.csv` | Catálogo auditable para estandarizar las entidades federativas |
| `datos_03.limpieza-datos.R` | Script de limpieza: produce `datos_04`, `datos_05` y `datos_08` |
| `datos_04.datos-limpios-completos.csv`, `.xlsx` y `.rds` | Datos limpios de las 113 respuestas |
| `datos_05.datos-interesados.csv` y `.rds` | Datos limpios de las 100 personas interesadas |
| `datos_06.diccionario-datos.xlsx` | Diccionario de datos: variables, recodificaciones, área disciplinaria, frecuencias y calidad de datos |
| `datos_07.reporte-validacion-limpieza.md` | Reporte de validación de la limpieza |
| `datos_08.sesion-r-reproducibilidad.txt` | Sesión de R de la corrida canónica |
| `datos_09.*` | Instaladores del entorno para Fedora, Ubuntu y Windows, e instrucciones |
| `datos_10.verificar-reproducibilidad.R` | Comprueba que la limpieza reproduce los datos limpios publicados |
| `datos_11.analisis-descriptivo.R` | Análisis descriptivo y bivariado: produce `datos_14` y las figuras de barras |
| `datos_12.figura-area-x-linea.R` | Genera la Figura 2 del manuscrito; se ejecuta después de `datos_11` |
| `datos_13.mapa-entidades.R` y `datos_13.geojson-entidades-mexico.geojson` | Mapas por entidad federativa y geometrías de las entidades |
| `datos_14.tablas-resultados.xlsx` | Tablas de resultados |
| `datos_15.figuras/` | Diecisiete figuras y cuatro salidas tabulares (ver su `README.md`) |
| `datos_16.mca-exploratorio.R` | Análisis de correspondencias múltiples |
| `datos_17.reporte-cifras-canonicas.R` y `.txt` | Reporte canónico de las cifras del manuscrito y su salida |
| `datos_18.sensibilidad-rq7.R` y `.txt` | Sensibilidad de RQ7 |
| `datos_19.verificacion-independiente.py` y `.txt` | Recálculo independiente en Python |

El plan de análisis está en el anexo A del material suplementario.

## Cómo reproducir

1. Instale el entorno con el script de `datos_09` que corresponda a su sistema (R 4.3 o posterior).
2. Desde esta carpeta, ejecute en este orden:

```
Rscript datos_03.limpieza-datos.R
Rscript datos_10.verificar-reproducibilidad.R
Rscript datos_11.analisis-descriptivo.R
Rscript datos_12.figura-area-x-linea.R
Rscript datos_13.mapa-entidades.R
Rscript datos_16.mca-exploratorio.R
Rscript datos_17.reporte-cifras-canonicas.R
Rscript datos_18.sensibilidad-rq7.R
python3 datos_19.verificacion-independiente.py
```

Los scripts sobrescriben sus salidas. Las cifras de los archivos que se distribuyen son las de la
corrida canónica (R 4.5.3, Fedora Linux 43); en otro entorno solo cambian la fecha, la descripción
de la sesión y el ancho con que se imprime la tabla de RQ7. La reproducción completa se verificó
también en R 4.3.3 y Ubuntu 24.04 (anexo G).

## Licencia

Creative Commons Atribución 4.0 Internacional (CC BY 4.0). Ver `LICENSE.txt`.
