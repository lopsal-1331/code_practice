import math

def build_cost_matrix(true_positions, measurements, max_cost=1000):
    '''
    Construye la matriz de coste cuadrada para el algoritmo Hungarian.

    true_positions: lista de posiciones reales [(x,y),...]
    measurements: lista total de mediciones [(x,y),...]
    max_cost: coste de no-asignación (coste alto para relleno)

    Devuelve:
        - cost_matrix: matriz cuadrada de costes (lista de listas)
    '''
    cost_matrix = []
    
    # Primero calculamos los costes reales
    for i in range(len(true_positions)): 
        row = []
        for m in range(len(measurements)): 
            cost = math.sqrt((true_positions[i][0]-measurements[m][0])**2 + 
                             (true_positions[i][1]-measurements[m][1])**2)
            row.append(cost)
        cost_matrix.append(row)
    
    # Ahora completamos la matriz para que sea cuadrada:
    rows = len(true_positions)
    cols = len(measurements)
    
    if rows > cols: 
        # Más objetos que mediciones: añadir columnas (max_cost)
        for i in range(rows):
            cost_matrix[i].extend([max_cost] * (rows - cols))
    
    elif cols > rows: 
        # Más mediciones que objetos: añadir filas (max_cost)
        for i in range(cols - rows):
            new_row = [max_cost] * cols
            cost_matrix.append(new_row)
    
    return cost_matrix


true_positions = [[10, 20], [30, 40]]
measurements = [[9, 21], [31, 39], [50, 50]]
cost_matrix = build_cost_matrix(true_positions, measurements)
for row in cost_matrix:
    print(row)
