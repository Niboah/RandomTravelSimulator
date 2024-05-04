import numpy as np

# Definir las dimensiones de la matriz y los números a asignar
num_rows = 25
num_cols = 25
negative_numbers = [-i for i in range(1, 18)]  # Generar 17 números negativos

# Crear una matriz vacía de 4x5
city_matrix = np.full((num_rows, num_cols), 0)

# Función para comprobar si la posición es válida
def is_valid_position(matrix, row, col, distance):
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
np.random.seed(2)

for num in negative_numbers:
    placed = False
    attempts = 0
    while not placed and attempts < 100:  # Limitar los intentos para evitar bucle infinito
        row = np.random.randint(0, num_rows)
        col = np.random.randint(0, num_cols)
        if is_valid_position(city_matrix, row, col, 3):  # Usar distancia
            city_matrix[row, col] = num
            placed = True
        attempts += 1

print(city_matrix)
