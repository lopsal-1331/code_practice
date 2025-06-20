'''
PRIMER RETO DE PROGRAMACIÓN 
Programamos una función que: 

    1) Genere N objetos en posiciones aleatorias
    2) Para cada objeto, genera una medición ruidosa
    3) Añade C detecciones falsas (clutter) aleatorias

'''

import random 
import numpy as np 

def generate_measurements(N_objects, C_clutter, noise_std, area_size) : 
    '''
    N_objects : número de objetos reales
    C_clutter : número de detecciones falsas
    noise_std : desviación estándar del ruido de medición
    area_size : tamaño del area cuadrada (lado)

    RETURN
        true_positions : lista de posiciones reales
        measurements : lista total de mediciones 
    '''
    true_positions = []
    measurements = []

    # Posiciones reales
    for i in range(N_objects): 
        x = random.randint(0, area_size-1)
        y = random.randint(0, area_size-1)
        true_positions.append([x,y])
    
    # mediciones con ruido
    for pos in true_positions: 
        x_meas = pos[0] + random.gauss(0, noise_std)
        y_meas = pos[1] + random.gauss(0, noise_std)
        measurements.append([x_meas, y_meas])
    
    # clutter
    for i in range(C_clutter): 
        x = random.randint(0, area_size-1)
        y = random.randint(0, area_size-1)
        measurements.append([x,y])
    
    return true_positions, measurements

tp, meas = generate_measurements(N_objects=3, C_clutter=5, noise_std=1.0, area_size=100)
print("True positions:", tp)
print("Measurements:", meas)

