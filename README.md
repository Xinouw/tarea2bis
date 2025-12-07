# Tarea 2 – Simulación y análisis de meteoros

Este repositorio contiene dos programas en Python que:

1. **Simulan** meteoros observados en una ventana de 2 días y guardan cada evento en un archivo de texto.
2. **Analizan** esos archivos para calcular el intervalo promedio de tiempo entre meteoros.

Todo se hace con **Python 3** y solo librerías estándar.

---

## 1. Contenido del repositorio

- `generate_meteors.py`  
  Script que genera archivos de texto `meteor_XXX.txt`, uno por cada meteoro simulado.

- `analyze_meteors.py`  
  Script que lee los archivos `meteor_XXX.txt` y crea el archivo de estadísticas `stats.txt`.

- `meteor_XXX.txt`  
  Algunos ejemplos de archivos de meteoros ya generados, uno por evento, en formato de texto plano.

- `stats.txt`  
  Archivo de salida con el número total de eventos y el intervalo de tiempo promedio entre meteoros.

---

## 2. Requisitos

- Python 3.x instalado (si se ejecuta en un PC local).
- No se usan librerías externas, solo:
  - `random`
  - `datetime`
  - `glob`

Si se usa **Google Colab**, no es necesario instalar nada extra.

---

## 3. Ejecución paso a paso en un PC local (terminal)

A continuación dejo los pasos como si partiera desde cero en un computador con Python instalado.

### 3.1. Clonar o descargar el repositorio

**Opción A: Clonar con git** (si tienes git instalado):

```bash
git clone https://github.com/Xinouw/tarea2bis.git
cd tarea2bis
