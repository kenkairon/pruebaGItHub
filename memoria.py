"""
Ejercicio 100
Obtener la cantidad de memoria Ram
en mi computadora o laptop
"""

# 1- pip install psutil

# 2- importar la libreria psutil
import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()
    
    memoria_total = memoria.total / (1024 ** 3)  # Convertir a GB
    return memoria_total

memoria = obtener_ram()

print(f"La memoria RAM total de la computadora es: {memoria:.2f} GB")