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
