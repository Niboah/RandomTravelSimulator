import random
def generate_unique_coordinates(size):
    coordinates = set()  # Use a set to store unique coordinates
    while len(coordinates) < 17:
        x = random.randint(*size)
        y = random.randint(*size)
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
    maxr=len(points);
    matrix = [[0] * 25 for _ in range(25)]
    i=0
    zeros=608
    for x,y in points:
        matrix[x][y]=i
        i+=1
    while zeros >0:
        p = random.randint(*17)
        x,y=points[p]
        nx,ny=find_adjacent_position_with_zero(matrix, x, y)
        points[p] = (nx, ny)
        matrix[nx][ny]=p
        zeros -=1


