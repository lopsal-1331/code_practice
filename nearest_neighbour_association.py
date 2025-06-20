import math 

def nearest_neighbour_association(true_positions, measurements, threshold):
    '''
    Asocia cada objeto a su medición más cercana.

    true_positions: lista de posiciones reales [(x,y),...]
    measurements: lista total de mediciones [(x,y),...]
    threshold: distancia máxima aceptable para asignar una medición

    Devuelve:
        - associations: lista de pares [(objeto_idx, medición_idx), ...]
    '''
    associations = []

    for i in range(len(true_positions)): 
        pos = true_positions[i]
        min_distance = float('inf')  # distancia mínima inicializada como infinito
        min_j = None  # índice de la medición más cercana

        for j in range(len(measurements)): 
            meas = measurements[j]
            x_pred = pos[0]
            y_pred = pos[1]
            x_meas = meas[0]
            y_meas = meas[1]

            # Calculamos la distancia euclídea
            distance = math.sqrt((x_pred - x_meas)**2 + (y_pred - y_meas)**2)

            if distance < min_distance: 
                min_distance = distance
                min_j = j
        
        # Solo aceptamos la asociación si la distancia es menor que el threshold
        if min_distance < threshold:
            associations.append((i, min_j))
    
    return associations


# Test de ejemplo
true_positions = [[10, 20], [30, 40], [50, 60]]
measurements = [[9, 21], [31, 39], [52, 61], [70, 80], [5, 5]]
threshold = 10.0

associations = nearest_neighbour_association(true_positions, measurements, threshold)
print("Associations:", associations)
