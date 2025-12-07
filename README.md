## Explicación del funcionamiento del programa

### 1. Script `generate_meteors.py`

Este programa se encarga de **simular** la lluvia de meteoros y guardar cada evento en un archivo de texto.

Paso a paso:

1. **Define la ventana de tiempo**  
   Se fijan dos fechas:
   - INICIO = `2025-12-01 02:00:00`
   - FIN    = `2025-12-03 02:00:00`  
   Esto corresponde a una ventana de 2 días donde se van a ubicar todos los meteoros.

2. **Elige cuántos meteoros simular**  
   Se usa `random.randint(500, 999)` para escoger un número entero entre 500 y 999.  
   Ese será el número total de archivos `meteor_XXX.txt` que se van a crear.

3. **Calcula el paso de tiempo entre meteoros**  
   - Se calcula la cantidad total de segundos entre INICIO y FIN.
   - Ese número de segundos se divide por la cantidad de eventos.  
   - Con esto se obtiene un `paso_segundos` que se usa para que cada meteoro ocurra unos segundos después del anterior.  
   Así se asegura que:
   - Los **timestamps son únicos**.
   - Los eventos quedan en **orden creciente** en el tiempo.
   - La distribución es aproximadamente uniforme dentro de los 2 días.

4. **Genera los datos de cada meteoro**  
   Para cada índice `indice`:
   - Se calcula el instante del meteoro sumando `indice * paso_segundos` a la fecha de INICIO.
   - Se generan al azar:
     - `duracion_segundos` ∈ [0.1, 5.0]
     - `altura_grados` ∈ [10.0, 90.0]
     - `acimut_grados` ∈ [0.0, 359.0]

5. **Crea el archivo `meteor_XXX.txt`**  
   - Se arma el nombre con 3 dígitos: `meteor_001.txt`, `meteor_002.txt`, etc.
   - Se escribe una sola línea en el archivo con el formato:
     ```text
     YYYY-MM-DD, HH:MM:SS, duracion_seg, altura_grados, acimut_grados
     ```

6. **Reproducibilidad**  
   Al inicio se fija una semilla con `random.seed(0)`.  
   Esto hace que, si se borra todo y se vuelve a ejecutar el script, se obtenga la misma secuencia de meteoros.

---

### 2. Script `analyze_meteors.py`

Este programa **lee** los archivos generados y calcula el **intervalo promedio de tiempo** entre meteoros.

Paso a paso:

1. **Busca todos los archivos `meteor_*.txt`**  
   Usa `glob.glob("meteor_*.txt")` para obtener la lista de archivos de meteoros en el directorio actual.

2. **Lee la marca de tiempo de cada archivo**  
   Para cada archivo:
   - Se lee la única línea que contiene.
   - Se separa la línea por comas.
   - Se toman las dos primeras partes: `fecha` y `hora`.
   - Se combinan en un string `"YYYY-MM-DD HH:MM:SS"` y se convierten a un objeto `datetime`.

3. **Ordena los eventos en el tiempo**  
   Todos los `datetime` se guardan en una lista y luego se ordenan con `instantes.sort()`, para asegurarse de que están en orden cronológico.

4. **Calcula las diferencias entre eventos consecutivos**  
   - Se recorre la lista de instantes desde el segundo elemento hasta el último.
   - Para cada par consecutivo se calcula `instantes[i] - instantes[i-1]`.
   - Cada diferencia se pasa a segundos con `.total_seconds()` y se guarda en una lista.

5. **Obtiene el intervalo promedio entre meteoros**  
   - Se suman todas las diferencias en segundos.
   - Se divide por la cantidad de diferencias (que es número_de_eventos - 1).  
   De esta forma se obtiene el **intervalo promedio entre meteoros en segundos**.

6. **Escribe el resumen en `stats.txt`**  
   Finalmente se crea el archivo `stats.txt` con el formato:
   ```text
   Total events: N
   Average time between meteors: X.X seconds



o


