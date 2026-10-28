#!/usr/bin/env python3
# =============================================================================
# datos_19.verificacion-independiente.py
# Recalculo independiente, en Python, de las cifras canonicas de datos_17 (R).
#
# Proposito: comprobar que las cifras del manuscrito no dependen de una sola
# implementacion. Se programa sin reutilizar el codigo de R y con un algoritmo
# de simulacion distinto: R usa r2dtable() (tablas aleatorias con margenes
# fijos); aqui se permutan las etiquetas de una de las dos variables, que
# genera la misma distribucion condicional por otra via. Las medidas
# deterministas deben coincidir digito por digito; los valores p simulados,
# dentro del error de simulacion.
#
# Entrada : datos_04.datos-limpios-completos.csv (113 registros)
# Salida  : datos_19.verificacion-independiente.txt
# Requiere: Python >= 3.10, numpy, scipy, pandas
# Uso     : python3 datos_19.verificacion-independiente.py
# =============================================================================
import math
import sys
import numpy as np
import pandas as pd
from scipy import stats
from scipy.special import gammaln

SEMILLA = 20260726
B = 200_000
B_RQ8 = 50_000
salida = []


def out(s=""):
    salida.append(s)
    print(s)


def clopper_pearson(k, n, nivel=0.95):
    a = 1 - nivel
    lo = stats.beta.ppf(a / 2, k, n - k + 1) if k > 0 else 0.0
    hi = stats.beta.ppf(1 - a / 2, k + 1, n - k) if k < n else 1.0
    return 100 * lo, 100 * hi


def v_cramer(tab):
    tab = np.asarray(tab, dtype=float)
    chi2 = stats.chi2_contingency(tab, correction=False)[0]
    n = tab.sum()
    return math.sqrt(chi2 / (n * (min(tab.shape) - 1)))


def log_prob_tabla(tab):
    """Log-probabilidad hipergeometrica multivariada de una tabla con margenes fijos."""
    tab = np.asarray(tab)
    filas, cols, n = tab.sum(1), tab.sum(0), tab.sum()
    return (gammaln(filas + 1).sum() + gammaln(cols + 1).sum()
            - gammaln(n + 1) - gammaln(tab + 1).sum())


def fisher_montecarlo(x, y, b, rng):
    """p de Fisher (r x c) por Monte Carlo, permutando y con x fijo."""
    cx, ix = np.unique(x, return_inverse=True)
    cy, iy = np.unique(y, return_inverse=True)
    r, c = len(cx), len(cy)
    obs = np.zeros((r, c), int)
    np.add.at(obs, (ix, iy), 1)
    # Con margenes fijos, la probabilidad de una tabla solo varia por -sum(log(n_ij!));
    # se cuenta como en R: tablas con estadistico <= observado / (1 + 64 eps).
    s_obs = -gammaln(obs + 1).sum()
    casi_1 = 1 + 64 * np.finfo(float).eps
    cuenta, hechos, lote = 0, 0, 20_000
    while hechos < b:
        m = min(lote, b - hechos)
        perm = np.argsort(rng.random((m, len(iy))), axis=1)
        iy_p = iy[perm]
        celdas = ix[None, :] * c + iy_p
        tabs = np.zeros((m, r * c), int)
        np.add.at(tabs, (np.repeat(np.arange(m), len(iy)), celdas.ravel()), 1)
        s_sim = -gammaln(tabs + 1).sum(1)
        cuenta += int(np.sum(s_sim <= s_obs / casi_1))
        hechos += m
    p = (1 + cuenta) / (b + 1)
    ee = math.sqrt(p * (1 - p) / b)
    return obs, p, ee


def esperadas_menores_5(tab):
    e = stats.contingency.expected_freq(np.asarray(tab, dtype=float))
    return 100 * np.mean(e < 5)


def logit_irls(x, y, iters=50):
    X = np.column_stack([np.ones_like(x, dtype=float), x.astype(float)])
    beta = np.zeros(2)
    for _ in range(iters):
        eta = X @ beta
        mu = 1 / (1 + np.exp(-eta))
        w = mu * (1 - mu)
        h = X.T @ (X * w[:, None])
        g = X.T @ (y - mu)
        paso = np.linalg.solve(h, g)
        beta += paso
        if np.max(np.abs(paso)) < 1e-12:
            break
    cov = np.linalg.inv(h)
    z = beta[1] / math.sqrt(cov[1, 1])
    return beta[1], z, 2 * stats.norm.sf(abs(z))


def mca_inercia(df):
    """Inercia de los dos primeros ejes del MCA (CA de la matriz indicadora)."""
    z = pd.get_dummies(df.astype(str)).to_numpy(dtype=float)
    n, q = z.shape[0], df.shape[1]
    p = z / z.sum()
    r, c = p.sum(1), p.sum(0)
    s = (p - np.outer(r, c)) / np.sqrt(np.outer(r, c))
    vs = np.linalg.svd(s, compute_uv=False) ** 2
    total = z.shape[1] / q - 1
    return vs[:2], 100 * vs[:2] / total, total


rng = np.random.default_rng(SEMILLA)
d = pd.read_csv("datos_04.datos-limpios-completos.csv", encoding="utf-8")
d = d.replace("NA", np.nan)
di = d[d["interes_en_doctorado"] == "Sí"].copy()

out("=" * 78)
out("VERIFICACION INDEPENDIENTE EN PYTHON DE LAS CIFRAS CANONICAS (datos_17, R)")
out("=" * 78)
out(f"Python {sys.version.split()[0]} | numpy {np.__version__} | pandas {pd.__version__} | scipy {__import__('scipy').__version__}")
out(f"Semilla {SEMILLA} | B = {B} (RQ6, RQ7) | B = {B_RQ8} (RQ8) | algoritmo: permutacion de etiquetas")
out()

k, n = len(di), len(d)
lo, hi = clopper_pearson(k, n)
out(f"RQ1  interes: {k}/{n} = {100*k/n:.1f} %  IC 95 % Clopper-Pearson [{lo:.2f}, {hi:.2f}]")

perm = int((di["estado_estudios"] == di["estado_residencia"]).sum())
lo, hi = clopper_pearson(perm, len(di))
out(f"RQ8  permanencia: {perm}/{len(di)} = {100*perm/len(di):.1f} %  IC 95 % [{lo:.2f}, {hi:.2f}]")
out()

g = pd.crosstab(d["genero"], d["interes_en_doctorado"])
_, pf = stats.fisher_exact(g.to_numpy())
chi = stats.chi2_contingency(g.to_numpy(), correction=False)[1]
out(f"Genero x interes (n = {n}): Fisher p = {pf:.4f} | ji cuadrada sin correccion p = {chi:.4f} | V = {v_cramer(g):.4f}")

edad_inf = d["edad"].str.extract(r"^(\d+)")[0].astype(float)
ok = edad_inf.notna()
y = (d.loc[ok, "interes_en_doctorado"] == "Sí").astype(int).to_numpy()
b1, z, p = logit_irls(edad_inf[ok].to_numpy(), y)
rho, prho = stats.spearmanr(edad_inf[ok], y)
out(f"Edad x interes: beta = {b1:+.5f} por anio | z = {z:.4f} | p = {p:.4f} | Spearman rho = {rho:+.4f}, p = {prho:.4f}")
out()

pruebas = [
    ("RQ6a situacion laboral x plazo", di.dropna(subset=["situacion_laboral"]), "situacion_laboral", "tiempo_inicio_doctorado", B),
    ("RQ6b situacion laboral x motivacion", di.dropna(subset=["situacion_laboral"]), "situacion_laboral", "motivacion_en_doctorado", B),
    ("RQ7  area x linea", di, "area_maestria", "doctorado_de_interes", B),
    ("RQ7  sensibilidad: areas con >= 5 casos", di[di["area_maestria"].isin(["Social", "Agronómica", "Otras"])], "area_maestria", "doctorado_de_interes", B),
    ("RQ8  entidad de estudios x residencia", di, "estado_estudios", "estado_residencia", B_RQ8),
]
for nombre, base, a, b_, nb in pruebas:
    tab, p, ee = fisher_montecarlo(base[a].to_numpy(), base[b_].to_numpy(), nb, rng)
    out(f"{nombre}: n = {tab.sum()} | tabla {tab.shape[0]} x {tab.shape[1]} | "
        f"esperadas < 5: {esperadas_menores_5(tab):.1f} % | p = {p:.4f} (ee {ee:.4f}) | V = {v_cramer(tab):.4f}")
out()

vars_mca = ["genero", "edad", "area_maestria", "situacion_laboral",
            "motivacion_en_doctorado", "tiempo_inicio_doctorado"]
m = di[vars_mca].dropna()
vp, pct, total = mca_inercia(m)
out(f"MCA (n = {len(m)}, 6 variables): valores propios {vp[0]:.3f} y {vp[1]:.3f} | "
    f"inercia {pct[0]:.2f} % + {pct[1]:.2f} % = {pct.sum():.2f} % (inercia total {total:.3f})")

with open("datos_19.verificacion-independiente.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(salida) + "\n")
