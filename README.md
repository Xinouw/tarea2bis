# Tarea 2 – Simulación y análisis de meteoros

Este repositorio contiene la solución a la Tarea 2, donde se pide simular una serie de meteoros observados en una ventana de 2 días y luego analizar esos datos para obtener el intervalo promedio entre eventos.

La idea general es:

- Primero **generar datos sintéticos** de meteoros y guardarlos en archivos de texto simples (`meteor_XXX.txt`).
- Después **leer esos archivos** y calcular cada cuántos segundos, en promedio, aparece un meteoro.

Todo está hecho en **Python 3** usando solo librerías estándar, tal como pide el enunciado.

---

## Estructura del repositorio

En la raíz del repositorio se encuentran los siguientes archivos principales:

- `generate_meteors.py`  
  Script que genera los archivos de meteoros `meteor_XXX.txt`.

- `analyze_meteors.py`  
  Script que lee los archivos de meteoros y construye el archivo de estadísticas `stats.txt`.

- `stats.txt`  
  Archivo de salida con el número total de eventos considerados y el intervalo de tiempo promedio entre meteoros.

- `meteor_XXX.txt`  
  Algunos archivos de ejemplo generados por `generate_meteors.py`.  
  Cada archivo corresponde a un meteoro y contiene una sola línea con sus datos (fecha, hora, duración y ángulos).



---

## Cómo ejecutar los programas

### Opción 1: Desde la terminal (Python local)

1. Ejecutar el script que genera los meteoros:

   ```bash
   python generate_meteors.py
