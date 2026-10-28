# ==============================================================================
# datos_18.sensibilidad-rq7.R
# Análisis de sensibilidad de la única asociación significativa (RQ7:
# área disciplinaria de la maestría x línea de doctorado), ante la exclusión de
# las categorías de área con menos de cinco casos.
# Usa solo R base. Misma función de prueba que datos_17 (semilla por prueba).
# Ejecutar desde la carpeta del repositorio, después de datos_03:
#   Rscript datos_18.sensibilidad-rq7.R
# ==============================================================================
invisible(try(Sys.setlocale("LC_ALL", "C.UTF-8"), silent = TRUE))
B <- 200000L
SEMILLA_BASE <- 20260726L
di <- read.csv("datos_05.datos-interesados.csv", stringsAsFactors = FALSE,
               fileEncoding = "UTF-8")
stopifnot(nrow(di) == 100L)

v_cramer <- function(tab) {
  ch <- suppressWarnings(chisq.test(tab, correct = FALSE))
  as.numeric(sqrt(ch$statistic / (sum(tab) * (min(dim(tab)) - 1))))
}
prueba <- function(tab, etiqueta, semilla) {
  ch <- suppressWarnings(chisq.test(tab, correct = FALSE))
  set.seed(semilla)
  p  <- fisher.test(tab, simulate.p.value = TRUE, B = B)$p.value
  cat(sprintf("\n%s\n   tabla %d x %d, n = %d | esperadas < 5: %.1f%%\n",
              etiqueta, nrow(tab), ncol(tab), sum(tab), 100 * mean(ch$expected < 5)))
  cat(sprintf("   Fisher simulado: p = %.4f (ee = %.5f) | B = %d | set.seed(%d)\n",
              p, sqrt(p * (1 - p) / B), B, semilla))
  cat(sprintf("   V de Cramér: %.4f\n", v_cramer(tab)))
  invisible(c(p = p, v = v_cramer(tab)))
}
cat("Versión de R:", R.version.string, "\n")
# (0) Réplica de la cifra canónica (misma semilla que datos_17: base + 3)
t7 <- table(di$area_maestria, di$doctorado_de_interes)
prueba(t7, "RQ7 canónica: 5 áreas x 8 líneas", SEMILLA_BASE + 3L)
print(t7)
# (1) Sensibilidad: se excluyen las áreas con menos de cinco casos
n_area <- table(di$area_maestria)
grandes <- names(n_area)[n_area >= 5]
cat("\nÁreas con >= 5 casos:", paste(grandes, collapse = ", "),
    "| excluidas:", paste(setdiff(names(n_area), grandes), collapse = ", "), "\n")
d1 <- di[di$area_maestria %in% grandes, ]
t1 <- table(d1$area_maestria, d1$doctorado_de_interes)
t1 <- t1[, colSums(t1) > 0, drop = FALSE]
prueba(t1, "Sensibilidad 1: áreas con >= 5 casos x líneas observadas", SEMILLA_BASE + 5L)
# (2) Sensibilidad: tres líneas del núcleo y 'otra' (respuesta libre agrupada)
nucleo <- c("Manejo y Aprovechamiento del Paisaje Rural",
            "Desarrollo del Paisaje Rural", "Paisaje y Turismo Rural")
l4 <- ifelse(d1$doctorado_de_interes %in% nucleo, d1$doctorado_de_interes, "Otra (respuesta libre)")
t2 <- table(d1$area_maestria, l4)
prueba(t2, "Sensibilidad 2: áreas con >= 5 casos x (tres líneas + otra)", SEMILLA_BASE + 6L)
# Proporción que elige Manejo y Aprovechamiento por área
cat("\nProporción que elige Manejo y Aprovechamiento del Paisaje Rural, por área:\n")
for (a in names(n_area)) {
  s <- di$area_maestria == a
  k <- sum(di$doctorado_de_interes[s] == nucleo[1])
  cat(sprintf("   %-12s %2d de %2d = %5.1f%%\n", a, k, sum(s), 100 * k / sum(s)))
}
