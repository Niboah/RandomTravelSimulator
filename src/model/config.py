from src.model.ExtractCities import genMatrix
from src.model.CalculateCityBetween import calculateCityBetween
from src.model.ReadCSV import DailyIteration
from src.utils.read_file import getCities

import numpy as np

def configure():
    num_rows = 40
    num_cols = 40
    unique_cities = getCities()

    matrix, points2 = genMatrix(num_rows,num_cols,len(unique_cities))

    negative_numbers = {unique_cities[i-1]:-i for i in range(1, len(unique_cities) + 1)}
    points = negative_numbers

    vector=[(0,1),(1,0),(0,-1),(-1,0)]
    zeros=num_rows*num_cols-17
    while zeros>0:
        for i in range (1,18):
            coordenadas = np.argwhere(matrix==-i)
            coordenadas2 = np.argwhere(matrix==i)
            coordenadas=np.concatenate((coordenadas,coordenadas2))
            for x,y in coordenadas:
                for xdir,ydir in vector:
                    nx=x+xdir
                    ny=y+ydir
                    if(nx>=0 and nx <num_rows and ny>=0 and ny <num_cols and matrix[nx,ny]==0):
                        matrix[nx,ny]=i
                        zeros-=1

    cityCoodinates = dict()
    unique_cities = list(unique_cities)
    for i in range (1,len(unique_cities)+1):
        cityCoodinates[unique_cities[i-1]] = (np.argwhere(matrix==-i)[0][0],np.argwhere(matrix==-i)[0][1])
    cityMiddle = calculateCityBetween(cityCoodinates, matrix)

    [EveryDay,_,allFlyer] = DailyIteration(cityMiddle)
    return unique_cities, matrix, points,points2,EveryDay,allFlyer