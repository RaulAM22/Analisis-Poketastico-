# =========================================
# PROYECTO LP – ANÁLISIS ESTADÍSTICO CON POKEAPI
# =========================================

# =========================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# =========================================

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

# =========================================
# 1. CONSUMO DE LA API (DANI)
# =========================================

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
LIMIT = 100

pokemon_raw = []

print("Obteniendo datos desde PokeAPI...")

for i in range(1, LIMIT + 1):
    r = requests.get(BASE_URL + str(i))
    if r.status_code == 200:
        pokemon_raw.append(r.json())

os.makedirs("data", exist_ok=True)
os.makedirs("figures", exist_ok=True)
os.makedirs("figures/pokemon_images", exist_ok=True)

with open("data/raw_pokemon.json", "w", encoding="utf-8") as f:
    json.dump(pokemon_raw, f, indent=4)

print(f"✔ Se obtuvieron {len(pokemon_raw)} Pokémon\n")

# =========================================
# 2. LIMPIEZA Y ESTRUCTURACIÓN (GIANE)
# =========================================

clean_data = []

for p in pokemon_raw:
    tipos = [t["type"]["name"] for t in p["types"]]
    tipos_str = " / ".join(tipos)

    imagen_url = p["sprites"]["front_default"]

    clean_data.append({
        "nombre": p["name"],
        "tipo": tipos_str,
        "altura": p["height"],
        "peso": p["weight"],
        "experiencia_base": p["base_experience"],
        "salud": p["stats"][0]["base_stat"],
        "ataque": p["stats"][1]["base_stat"],
        "defensa": p["stats"][2]["base_stat"],
        "imagen": imagen_url
    })

    if imagen_url:
        img = requests.get(imagen_url).content
        with open(f"figures/pokemon_images/{p['name']}.png", "wb") as f:
            f.write(img)

df = pd.DataFrame(clean_data)
df.to_csv("data/pokemon_clean.csv", index=False, encoding="utf-8")

# =========================================
# TRADUCCIÓN DE TIPOS
# =========================================

traduccion_tipos = {
    "normal": "Normal",
    "fire": "Fuego",
    "water": "Agua",
    "electric": "Eléctrico",
    "grass": "Planta",
    "ice": "Hielo",
    "fighting": "Lucha",
    "poison": "Veneno",
    "ground": "Tierra",
    "flying": "Volador",
    "psychic": "Psíquico",
    "bug": "Bicho",
    "rock": "Roca",
    "ghost": "Fantasma",
    "dark": "Siniestro",
    "dragon": "Dragón",
    "steel": "Acero",
    "fairy": "Hada"
}


# =========================================
# 3. ESTADÍSTICA DESCRIPTIVA (LARRY)
# =========================================

desc = df.describe().round(2)
print(desc)


# =========================================
# 3.1 MEDIDAS ESTADÍSTICAS (LARRY)
# =========================================

means_df = df[["salud", "ataque", "defensa"]].mean().to_frame("Media")
medians_df = df[["salud", "ataque", "defensa"]].median().to_frame("Mediana")
std_df = df[["salud", "ataque", "defensa"]].std().to_frame("Desviación Estándar")


def save_table_image(df_table, title, path):
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.axis("off")
    ax.table(
        cellText=df_table.round(2).values,
        colLabels=df_table.columns,
        rowLabels=df_table.index,
        loc="center"
    )
    plt.title(title)
    plt.savefig(path, bbox_inches="tight")
    plt.close()


save_table_image(means_df, "Media de Estadísticas", "figures/tabla_medias.png")
save_table_image(medians_df, "Mediana de Estadísticas", "figures/tabla_medianas.png")
save_table_image(std_df, "Desviación Estándar", "figures/tabla_desviacion.png")

# =========================================
# 3.1 ESTADÍSTICAS CUALITATIVAS – TIPOS (MEGUMI)
# =========================================

print("📊 ESTADÍSTICAS CUALITATIVAS: TIPO DE POKÉMON\n")

types_expanded = df["tipo"].str.split(" / ").explode()

tabla_frecuencia = types_expanded.value_counts().to_frame(name='Frecuencia Absoluta')
tabla_frecuencia['Porcentaje (%)'] = (types_expanded.value_counts(normalize=True) * 100).round(2)
tabla_frecuencia.index.name = 'Tipo'

print("📌 Tabla de Distribución de Frecuencias:")
print(tabla_frecuencia)
# =========================================
pokemon_colors = {
    'poison': '#A33EA1',   # Veneno
    'bug': '#A6B91A',      # Bicho
    'normal': '#A8A77A',   # Normal
    'flying': '#A98FF3',   # Volador
    'grass': '#7AC74C',    # Planta
    'fire': '#EE8130',     # Fuego
    'ground': '#E2BF65',   # Tierra
    'fairy': '#D685AD',    # Hada
    'water': '#6390F0',    # Agua
    'electric': '#F7D02C', 
    'fighting': '#C22E28',
    'psychic': '#F95587',
    'rock': '#B6A136',
    'ghost': '#735797',
    'ice': '#96D9D6',
    'dragon': '#6F35FC',
    'steel': '#B7B7CE',
    'dark': '#705746'
}

# =========================================
# GENERAR EL GRÁFICO
# =========================================
plt.figure(figsize=(12, 8))

grafico = sns.countplot(
    y=types_expanded,                          
    order=types_expanded.value_counts().index, 
    palette=pokemon_colors,          
    edgecolor='black', linewidth=0.5          
)

plt.title('Distribución de Tipos de Pokémon', fontsize=16, fontweight='bold')
plt.xlabel('Cantidad de Pokémon', fontsize=12)
plt.ylabel('Tipo Elemental', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Añadir los números al final de las barras 
for container in grafico.containers:
    grafico.bar_label(container, padding=3, fontweight='bold', fmt='%d')

plt.show()

# =========================================
# 4. GRÁFICOS DESCRIPTIVOS
# =========================================
freq_types = types_expanded.value_counts()


plt.figure(figsize=(10,5))
freq_types.plot(kind="bar", edgecolor="black")
plt.title("Frecuencia de Tipos de Pokémon")
plt.xlabel("Tipo")
plt.ylabel("Cantidad")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("figures/frecuencia_tipos.png")
plt.show()

# =========================================
# 5. GRÁFICOS COMPARATIVOS (RAÚL)
# =========================================

plt.figure(figsize=(7,4))

data = [df["salud"], df["ataque"], df["defensa"]]
labels = ["Salud", "Ataque", "Defensa"]

plt.boxplot(
    data,
    labels=labels,
    patch_artist=True,
    showmeans=True,
    meanprops={
        "marker": "o",
        "markerfacecolor": "red",
        "markeredgecolor": "black",
        "markersize": 7
    }
)

plt.title("Comparación de Estadísticas Base")
plt.ylabel("Valor")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.savefig("figures/boxplot_stats.png")
plt.show()

# =========================================
# 6.1 ÍNDICE DE PODER Y RANKING (DANI)
# =========================================

df["indice_poder"] = (
    0.4 * df["ataque"] +
    0.3 * df["defensa"] +
    0.3 * df["salud"]
).round(2)

top10_poder = df.sort_values("indice_poder", ascending=False).head(10)
print(top10_poder)

# =========================================
# 6.2 COMPARACIÓN POR TIPO (GIANE)
# =========================================

df_tipos = df.copy()
df_tipos["tipo"] = df_tipos["tipo"].str.split(" / ")
df_tipos = df_tipos.explode("tipo")
df_tipos["tipo"] = df_tipos["tipo"].map(traduccion_tipos)

promedios_por_tipo = (
    df_tipos
    .groupby("tipo")[["salud", "ataque", "defensa", "indice_poder"]]
    .mean()
    .round(2)
    .sort_values(by="indice_poder", ascending=False)
)

print(promedios_por_tipo)

# =========================================
# 6.3 VISUALIZACIÓN – ÍNDICE DE PODER (LARRY)
# =========================================

plt.figure(figsize=(10,5))
promedios_por_tipo["indice_poder"].plot(kind="bar", edgecolor="black")
plt.title("Índice de Poder Promedio por Tipo")
plt.xlabel("Tipo")
plt.ylabel("Índice de Poder")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("figures/indice_poder_por_tipo.png")
plt.show()



#========================================
# CONCLUSIÓN
#========================================
print("""
CONCLUSIÓN DEL PROYECTO

El presente código desarrolla un análisis estadístico completo de los primeros 100 Pokémon
utilizando datos obtenidos directamente desde la PokeAPI. En una primera etapa, se realiza
el consumo de la API para recolectar información relevante como nombre, tipo, peso, altura,
experiencia base, estadísticas de combate y sprites oficiales, los cuales son almacenados
tanto en formato JSON como en un archivo CSV estructurado.

Posteriormente, los datos son limpiados y organizados en un DataFrame, lo que permite aplicar
estadística descriptiva sobre variables cuantitativas clave como salud, ataque y defensa.
Se calculan medidas de tendencia central y dispersión (media, mediana y desviación estándar),
facilitando una comprensión general del comportamiento de las estadísticas base de los Pokémon.

Además, se realiza un análisis cualitativo del tipo elemental, construyendo tablas de frecuencia
y gráficos que muestran la distribución de tipos, permitiendo identificar los tipos más comunes
dentro de la muestra analizada. Estos resultados son reforzados mediante visualizaciones claras
y comparativas.

Finalmente, se define un índice de poder que combina ataque, defensa y salud, lo que permite
establecer un ranking de los Pokémon más fuertes y comparar el poder promedio entre los distintos
tipos elementales. En conjunto, este proyecto demuestra cómo el uso de APIs, Python y técnicas
estadísticas puede transformar datos crudos en información significativa, visual y útil para
la toma de decisiones y el análisis exploratorio.
""")


