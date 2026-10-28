# Instrumento y diccionario de datos

**Se cita en:** apartados 2.3, 2.5 y 2.7 del manuscrito, como Autor/a (s.f.).
**Archivos:** `repositorio/datos_00.instrumento-cuestionario.docx` (fuente oficial) y `repositorio/datos_06.diccionario-datos.xlsx`.

## Instrumento de levantamiento de datos

**Cuestionario de Demanda potencial para Doctorado en Ciencias**

El presente cuestionario tiene como finalidad obtener información, con fines estadísticos,
para determinar la demanda potencial para la apertura de un Doctorado en Ciencias orientado
al paisaje y turismo rural, desarrollo, manejo y/o aprovechamiento del paisaje rural.
Agradecemos su valiosa aportación.

1. **Le interesa cursar un Doctorado en:**
   - Paisaje y Turismo Rural
   - Desarrollo del Paisaje Rural
   - Manejo y Aprovechamiento del Paisaje Rural
   - Otro: _______________

2. **Género:**
   - Femenino
   - Masculino

3. **Edad (por rangos):**
   21 a 25 · 26 a 30 · 31 a 35 · 36 a 40 · 41 a 45 · 46 a 50 · 51 a 55 · 56 a 60 · 61 y más

4. **¿En qué estado de la República Mexicana realiza o realizó sus estudios de Maestría?** (texto libre)

5. **¿En qué estado de la República Mexicana se encuentra radicando actualmente?** (texto libre)

6. **Nombre de la Maestría que estudia o estudió:** (texto libre)

7. **Nombre de la institución donde realiza o realizó sus estudios de Maestría:** (texto libre)

8. **¿Cuál es su situación laboral?**
   - Trabaja y estudia
   - Trabajo como docente
   - Trabajo como empleado
   - Negocio propio
   - Solo estudia
   - Otro. Por favor, indique cuál: _______________

9. **¿Cuál es su interés por estudiar un Doctorado? Dedicarse a:**
   - Investigación
   - Docencia
   - Aplicación en campo
   - Otro: _______________

10. **¿En qué tiempo podría iniciar los estudios de Doctorado?**
    - De inmediato · En 1 año · En 2 años · En 3 años · En 4 años · En 5 años · Indefinido

---

### Nota de trazabilidad entre instrumento y datos

El formulario aplicado en línea (Google Forms) incluyó, además, una **pregunta filtro
Sí/No** de interés general en el doctorado —capturada en la variable `interes_en_doctorado`—
que **no aparece como ítem independiente en el instrumento en Word**. Es decir, ese documento recoge
el cuerpo de preguntas de contenido, pero no reproduce con exactitud la lógica de salto
("skip logic") del formulario en línea. Se deja constancia de esta diferencia por
transparencia metodológica; no afecta la validez de los datos, solo su documentación.
Ver hallazgo correspondiente en `datos_07.reporte-validacion-limpieza.md`.

## Diccionario de datos: variables

El diccionario completo, con las recodificaciones valor por valor, la correspondencia con el área
disciplinaria, las frecuencias y la auditoría de calidad, está en `repositorio/datos_06.diccionario-datos.xlsx`.

| Variable | Origen | Valores en los datos limpios (n sobre 113) | Faltantes |
|---|---|---|---:|
| `marca_temporal` | Automática del formulario en línea | De 2024-04-04 20:10 a 2024-05-07 14:53 | 0 |
| `interes_en_doctorado` | Pregunta filtro del formulario en línea; no figura como reactivo numerado en datos_00 (hallazgo 1 de datos_07) | Sí (100) · No (13) | 0 |
| `doctorado_de_interes` | Reactivo 1, con opción «Otro» | Manejo y Aprovechamiento del Paisaje Rural (55) · Desarrollo del Paisaje Rural (17) · Paisaje y Turismo Rural (17) · Desarrollo rural (6) · Desarrollo Regional (2) · Energías (1) · Sociología (1) · Urbanismo y Relaciones de Poder (1) | 13 |
| `genero` | Reactivo 2 | Femenino (66) · Masculino (47) | 0 |
| `edad` | Reactivo 3 | 26 a 30 (38) · 31 a 35 (24) · 36 a 40 (12) · 51 a 55 (11) · 21 a 25 (8) · 41 a 45 (7) · 46 a 50 (7) · 56 a 60 (4) · 61 o más (2) | 0 |
| `estado_estudios` | Reactivo 4 | 17 entidades; ver la hoja Frecuencias | 0 |
| `estado_residencia` | Reactivo 5 | 24 lugares, incluida la residencia en el extranjero; ver la hoja Frecuencias | 0 |
| `area_maestria` | Derivada del reactivo 6 | Social (53) · Agronómica (32) · Otras (22) · Economía (4) · Alimentos (2) | 0 |
| `maestria_estudiada` | Reactivo 6 | 31 cadenas distintas (29 sin distinguir acentos, mayúsculas ni erratas de captura) | 0 |
| `universidad_estudios_maestria` | Reactivo 7 | Códigos I01 a I20 | 0 |
| `situacion_laboral` | Reactivo 8 | Solo estudia (38) · Docente (24) · Trabaja y estudia (23) · Empleado (21) · Negocio propio (5) | 2 |
| `motivacion_en_doctorado` | Reactivo 9, con opción «Otro» | Investigación (61) · Docencia (31) · Aplicación en campo (18) · Otro (3) | 0 |
| `tiempo_inicio_doctorado` | Reactivo 10 | En 1 año (60) · Indefinido (24) · En 2 años (19) · En 3 años (9) · En 5 años (1) | 0 |
| `motivacion_en_doctorado_otro_texto` | Reactivo 9, opción «Otro» | Ninguno (1) · Sector privado (1) · no tengo interés , estoy por jubilarme (1) | 110 |

En esta versión para arbitraje, `universidad_estudios_maestria` contiene el código de institución del
anexo B; el resto de los valores es el de los datos originales.
