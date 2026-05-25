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

    inicio = datetime.datetime.now()

    print("\nHora de inicio:",
          inicio.strftime("%d/%m/%Y %H:%M:%S"))

    return lista_loss, lista_latencias


def analizar_rendimiento(lista_loss):
    pass


def calcular_rmse(predicciones, reales):
    pass


# ==========================================
# 4. PROGRAMA PRINCIPAL
# ==========================================

if __name__ == "__main__":
    print("=== INICIANDO SIMULADOR ===")