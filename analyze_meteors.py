# analyze_meteors.py
import glob
from datetime import datetime

def analizar_meteoros():
    """
    Lee todos los archivos meteor_*.txt, ordena los eventos por tiempo
    y calcula el intervalo promedio entre meteoros (en segundos).

    El resultado se guarda en stats.txt con el formato:
    Total events: N
    Average time between meteors: X.X seconds
    """

    instantes = []

    # 1) Buscar todos los archivos meteor_*.txt en el directorio actual
    for nombre_archivo in sorted(glob.glob("meteor_*.txt")):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            linea = archivo.readline().strip()

        if not linea:
            # Si el archivo está vacío, lo saltamos
            continue

        # 2) Separar la línea por comas
        partes = [texto.strip() for texto in linea.split(",")]

        # Formato esperado:
        # fecha, hora, duración_seg, altura_grados, acimut_grados
        fecha_str = partes[0]
        hora_str  = partes[1]

        # 3) Convertir fecha+hora a un objeto datetime
        instante = datetime.strptime(
            fecha_str + " " + hora_str,
            "%Y-%m-%d %H:%M:%S"
        )
        instantes.append(instante)

    # Total de eventos encontrados
    total_eventos = len(instantes)

    # 4) Calcular el intervalo promedio entre meteoros
    if total_eventos < 2:
        intervalo_promedio = 0.0
    else:
        # Ordenamos los instantes por si acaso
        instantes.sort()

        # Diferencias en segundos entre eventos consecutivos
        diferencias = []
        for i in range(1, total_eventos):
            delta = instantes[i] - instantes[i - 1]
            diferencias.append(delta.total_seconds())

        # Promedio de las diferencias
        intervalo_promedio = sum(diferencias) / len(diferencias)

    # 5) Guardar el resultado en stats.txt
    with open("stats.txt", "w", encoding="utf-8") as archivo_salida:
        archivo_salida.write(f"Total events: {total_eventos}\n")
        archivo_salida.write(
            f"Average time between meteors: {intervalo_promedio:.1f} seconds\n"
        )

    print("Se creó el archivo stats.txt con las estadísticas.")

# Punto de entrada si se ejecuta como script
if __name__ == "__main__":
    analizar_meteoros()
Add analyze_meteors.py
