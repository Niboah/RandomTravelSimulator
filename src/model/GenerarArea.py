import random
import numpy as np
def generate_unique_coordinates(size):
    coordinates = set()  # Use a set to store unique coordinates
    while len(coordinates) < 17:
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        coordinates.add((x, y))
    vector=[]
    for x,y in coordinates:
        vector.append((x,y))
    return vector

def find_adjacent_position_with_zero(matrix, x, y):
    for i in range(max(0, x - 1), min(x + 2, len(matrix))):
        for j in range(max(0, y - 1), min(y + 2, len(matrix[0]))):
            if (i, j) != (x, y) and matrix[i][j] == 0:
                return (i, j)
    return None
def expansion(points):
    matrix = [[0] * 25 for _ in range(25)]
    i = 1
    zeros = 25 * 25 - len(points)
    zero_positions = [(x, y) for x in range(25) for y in range(25) if (x, y) not in points]
    random.shuffle(zero_positions)

    for x, y in points:
        matrix[x][y] = i
        i += 1

    while zeros > 0:
        p = random.randint(0, 16)
        x, y = points[p]
        np = find_adjacent_position_with_zero(matrix, x, y)
        if np is not None:
            nx, ny = np
            points[p] = (nx, ny)
            matrix[nx][ny] = p+1
            zeros -= 1
        elif zero_positions:
            nx, ny = zero_positions.pop()
            points[p] = (nx, ny)
            matrix[nx][ny] = p+1
            zeros -= 1
        else:
            break  # No more zero positions available

    return matrix


points=generate_unique_coordinates(25)
mat=expansion(points)
print(mat)