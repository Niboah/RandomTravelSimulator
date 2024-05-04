import numpy as np



# Función para comprobar si la posición es válida
def is_valid_position(matrix, row, col, distance,num_rows,num_cols):
    row_start = max(0, row - distance)
    row_end = min(num_rows, row + distance + 1)
    col_start = max(0, col - distance)
    col_end = min(num_cols, col + distance + 1)
    
    # Revisar si alguna posición en el bloque está ocupada
    for r in range(row_start, row_end):
        for c in range(col_start, col_end):
            if matrix[r, c] != 0:
                return False
    return True

# Intentar colocar cada número respetando la distancia mínima de 3 bloques
def genMatrix(num_rows,num_cols,numCities):
    negative_numbers = [-i for i in range(1, numCities+1)]
    city_matrix = np.full((num_rows, num_cols), 0)

    point2 = {}

    for num in negative_numbers:
        placed = False
        attempts = 0
        while not placed and attempts < 100:  # Limitar los intentos para evitar bucle infinito
            row = np.random.randint(0, num_rows)
            col = np.random.randint(0, num_cols)
            if is_valid_position(city_matrix, row, col, 3,num_rows,num_cols):  # Usar distancia
                city_matrix[row, col] = num
                placed = True
                point2[num]=(col,row)
            attempts += 1
            

    return city_matrix, point2
