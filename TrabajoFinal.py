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