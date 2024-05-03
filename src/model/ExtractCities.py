import numpy as np

# Lista de ciudades única
unique_cities = ['Amsterdam', 'Barcelona', 'Berlin', 'Brussels', 'Budapest', 'Dublin', 'Florence', 
                 'Lisbon', 'London', 'Madrid', 'Milan', 'Munich', 'Paris', 'Prague', 'Rome', 'Vienna', 'Zurich']

# Definir las dimensiones de la matriz
num_rows = 25
num_cols = 25

# Crear una matriz vacía de 4x5
city_matrix = np.empty((num_rows, num_cols), dtype=object)

# Generar números enteros negativos para cada ciudad
negative_numbers = [-i for i in range(1, len(unique_cities) + 1)]

# Colocar números únicos en posiciones aleatorias en la matriz
np.random.seed(42)  # Para reproducibilidad
city_indices = np.random.choice(num_rows * num_cols, size=len(unique_cities), replace=False)
for idx, num in zip(city_indices, negative_numbers):
    row = idx // num_cols  # Calcular la fila
    col = idx % num_cols   # Calcular la columna
    city_matrix[row, col] = num

# Posiciones que no fueron seleccionadas se quedan como None
print(city_matrix)
