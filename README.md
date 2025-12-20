# 📊 Proyecto LP – Análisis Estadístico con PokeAPI

## 📌 Descripción
Este proyecto realiza un **análisis estadístico y exploratorio** de los primeros **100 Pokémon**, utilizando datos obtenidos directamente desde la **PokeAPI**.  
El objetivo es transformar datos crudos provenientes de una API en **información estructurada, visual y significativa**, aplicando estadística descriptiva y visualización de datos en Python.

---

## 🧠 Objetivos del Proyecto
- Consumir datos desde una API pública (PokeAPI)
- Limpiar y estructurar datos en formatos JSON y CSV
- Aplicar estadística descriptiva (media, mediana, desviación estándar)
- Analizar la distribución de tipos de Pokémon
- Crear visualizaciones claras y comparativas
- Construir un **índice de poder** para ranking y comparación entre tipos

---

## 🛠️ Tecnologías Utilizadas
- **Python 3**
- **Requests** – consumo de la API
- **Pandas** – manipulación de datos
- **Matplotlib & Seaborn** – visualización de datos
- **JSON & CSV** – almacenamiento de datos

---

## 📂 Estructura del Proyecto
📦 proyecto-pokeapi
┣ 📂 data
┃ ┣ raw_pokemon.json
┃ ┗ pokemon_clean.csv
┣ 📂 figures
┃ ┣ 📂 pokemon_images
┃ ┣ tabla_medias.png
┃ ┣ tabla_medianas.png
┃ ┣ tabla_desviacion.png
┃ ┣ frecuencia_tipos.png
┃ ┣ boxplot_stats.png
┃ ┗ indice_poder_por_tipo.png
┣ 📜 main.py
┗ 📜 README.md


---

## 🔄 Flujo del Proyecto

### 1️⃣ Consumo de la API
Se obtienen los datos de los primeros **100 Pokémon** desde la PokeAPI, almacenándolos en un archivo `JSON`.

### 2️⃣ Limpieza y Estructuración
- Selección de variables relevantes
- Creación de un DataFrame
- Exportación a CSV
- Descarga de imágenes oficiales de cada Pokémon

### 3️⃣ Estadística Descriptiva
Se analizan las variables cuantitativas:
- Salud
- Ataque
- Defensa  

Incluye:
- Media
- Mediana
- Desviación estándar

### 4️⃣ Análisis Cualitativo
- Distribución de tipos de Pokémon
- Tabla de frecuencias absolutas y porcentajes
- Gráficos de barras y conteo

### 5️⃣ Visualizaciones Comparativas
- Boxplots para comparar estadísticas base
- Gráficos de frecuencia por tipo

### 6️⃣ Índice de Poder
Se define un índice ponderado:
Índice de Poder = 0.4 * Ataque + 0.3 * Defensa + 0.3 * Salud


Permite:
- Ranking Top 10 Pokémon más fuertes
- Comparación del poder promedio por tipo elemental

---

## 📈 Resultados Destacados
- Identificación de los tipos más frecuentes
- Comparación clara entre estadísticas base
- Ranking de Pokémon según su índice de poder
- Tipos elementales con mayor poder promedio

---

## 🧾 Conclusión
Este proyecto demuestra cómo el uso de **APIs, Python y análisis estadístico** permite transformar grandes volúmenes de datos en información clara, visual y útil.  
La combinación de estadística descriptiva, visualización y métricas personalizadas como el índice de poder facilita el análisis exploratorio y la toma de decisiones basadas en datos.

---

## 👥 Créditos
Proyecto desarrollado de manera colaborativa por el equipo:
- Dani
- Giane
- Larry
- Megumi
- Raúl
- Fabricio :D
---



