# ==============================================================================
# datos_12.figura-area-x-linea.R
# Figura 2 del manuscrito: línea temática de interés según el área disciplinaria
# de la maestría (fig13_area_x_linea.png). Sustituye, para este cruce, la versión
# genérica que genera datos_11.analisis-descriptivo.R, por lo que se ejecuta
# después de ese script. Respecto de la versión genérica:
#   1. el área «Economía» se rotula «Económica», como en la Tabla 2 y en los
#      apartados 2.3 y 3.8 (reúne economía, finanzas e integración económica;
#      los programas de administración están en «Otras»);
#   2. el eje muestra el tamaño de cada área (n por categoría);
#   3. la leyenda va en dos columnas.
# Además ordena las líneas (tres del núcleo primero, luego respuesta libre) y
# usa la paleta Okabe-Ito, legible para personas con daltonismo.
# Usa solo ggplot2 y R base. Ejecutar desde la carpeta del repositorio.
# ==============================================================================
invisible(try(Sys.setlocale("LC_ALL", "C.UTF-8"), silent = TRUE))
suppressPackageStartupMessages(library(ggplot2))
di <- read.csv("datos_05.datos-interesados.csv", stringsAsFactors = FALSE,
               fileEncoding = "UTF-8")
stopifnot(nrow(di) == 100L)
dir_figuras <- "datos_15.figuras"
dir.create(dir_figuras, showWarnings = FALSE)

etq_area <- c("Social" = "Social", "Agronómica" = "Agronómica", "Otras" = "Otras",
              "Economía" = "Económica", "Alimentos" = "Alimentos")
nucleo <- c("Manejo y Aprovechamiento del Paisaje Rural",
            "Desarrollo del Paisaje Rural", "Paisaje y Turismo Rural")
libres <- c("Desarrollo rural", "Desarrollo Regional", "Energías", "Sociología",
            "Urbanismo y Relaciones de Poder")
stopifnot(all(di$doctorado_de_interes %in% c(nucleo, libres)),
          all(di$area_maestria %in% names(etq_area)))

tab <- as.data.frame(table(area = di$area_maestria, linea = di$doctorado_de_interes),
                     stringsAsFactors = FALSE)
tab <- tab[tab$Freq > 0, ]
n_area <- table(di$area_maestria)
orden_area <- names(sort(n_area))                       # menor a mayor: el mayor arriba
tab$area_lbl <- factor(sprintf("%s (n = %d)", etq_area[tab$area], as.integer(n_area[tab$area])),
                       levels = sprintf("%s (n = %d)", etq_area[orden_area], as.integer(n_area[orden_area])))
tab$linea <- factor(tab$linea, levels = c(nucleo, libres))

paleta <- c("Manejo y Aprovechamiento del Paisaje Rural" = "#0072B2",
            "Desarrollo del Paisaje Rural" = "#56B4E9",
            "Paisaje y Turismo Rural" = "#009E73",
            "Desarrollo rural" = "#E69F00",
            "Desarrollo Regional" = "#F0E442",
            "Energías" = "#CC79A7",
            "Sociología" = "#D55E00",
            "Urbanismo y Relaciones de Poder" = "#999999")

p <- ggplot(tab, aes(x = area_lbl, y = Freq, fill = linea)) +
  geom_col(position = position_fill(reverse = TRUE), width = 0.75,
           color = "white", linewidth = 0.2) +
  scale_y_continuous(labels = function(x) paste0(round(100 * x), "%"),
                     expand = expansion(mult = c(0, 0.01))) +
  scale_fill_manual(values = paleta, drop = FALSE) +
  coord_flip() +
  labs(x = NULL, y = "Porcentaje dentro de cada área disciplinaria", fill = NULL,
       subtitle = paste0("n = ", nrow(di))) +
  guides(fill = guide_legend(ncol = 2, byrow = FALSE)) +
  theme_minimal(base_size = 11, base_family = "Times") +
  theme(legend.position = "bottom",
        legend.text = element_text(family = "Times", size = 9.5),
        legend.key.size = unit(0.45, "cm"),
        panel.grid.minor = element_blank(),
        panel.grid.major.y = element_blank(),
        plot.subtitle = element_text(size = 9.5, color = "gray30", family = "Times"),
        plot.margin = margin(6, 14, 6, 6))

ggsave(file.path(dir_figuras, "fig13_area_x_linea.png"), p,
       width = 7.5, height = 5.2, dpi = 300, bg = "white")
cat("[OK] fig13_area_x_linea.png generada (Figura 2 del manuscrito)\n")
