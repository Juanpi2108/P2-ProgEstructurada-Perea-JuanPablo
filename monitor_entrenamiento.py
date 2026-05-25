"""
Nombre del Alumno: Juan Pablo Perea Lara
Matrícula: UX25II181
Fecha: 25/05/2026
Examen Segundo Parcial - Programación Estructurada
"""

# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================

import datetime
import math
import random
import statistics
import sys

# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================

MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95

# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================

def obtener_info_sistema():
    print("\n=== INFORMACIÓN DEL SISTEMA ===")

    print("Plataforma:", sys.platform)

    print("Versión de Python:", sys.version)

    print("Argumentos del sistema:", sys.argv)


def simular_metricas_entrenamiento(cantidad_epochs):
    lista_loss = []
    lista_latencias = []

    eventos = [
        "Epoch exitoso",
        "Gradiente inestable",
        "Actualización de pesos",
        "Sincronización completada"
    ]

    inicio = datetime.datetime.now()

    print("\n=== INICIO DEL ENTRENAMIENTO ===")

    print("Hora de inicio:",
          inicio.strftime("%d/%m/%Y %H:%M:%S"))

    for epoch in range(1, cantidad_epochs + 1):

        loss = random.uniform(0.10, 1.00)

        probabilidad_exito = random.random()

        evento = random.choice(eventos)

        latencia = random.uniform(0.5, 2.5)

        lista_loss.append(loss)
        lista_latencias.append(latencia)

        print("\nEpoch:", epoch)
        print("Loss:", round(loss, 4))
        print("Probabilidad de éxito:", round(probabilidad_exito, 4))
        print("Evento:", evento)
        print("Latencia:", round(latencia, 2))

        if loss >= UMBRAL_ERROR_CRITICO:

            print("\nERROR CRÍTICO DETECTADO")

            sys.exit()

    fin = datetime.datetime.now()

    tiempo_total = fin - inicio

    print("\nHora final:",
          fin.strftime("%d/%m/%Y %H:%M:%S"))

    print("Duración total:", tiempo_total)

    return lista_loss, lista_latencias


def analizar_rendimiento(lista_loss, lista_latencias):
    print("\n=== ANÁLISIS DE RENDIMIENTO ===")

    promedio_loss = statistics.mean(lista_loss)

    desviacion_loss = statistics.stdev(lista_loss)

    mediana_latencia = statistics.median(lista_latencias)

    print("Promedio de loss:", round(promedio_loss, 4))

    print("Desviación estándar:", round(desviacion_loss, 4))

    print("Mediana de latencia:", round(mediana_latencia, 4))


def calcular_rmse(predicciones, reales):
    suma = 0

    for i in range(len(predicciones)):
        diferencia = predicciones[i] - reales[i]
        cuadrado = math.pow(diferencia, 2)
        suma = suma + cuadrado
    promedio = suma / len(predicciones)

    rmse = math.sqrt(promedio)

    epochs_redondeados = math.ceil(rmse)

    print("\n=== CÁLCULO RMSE ===")

    print("RMSE:", round(rmse, 4))

    print("RMSE redondeado:", epochs_redondeados)


# ==========================================
# 4. PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR ===")