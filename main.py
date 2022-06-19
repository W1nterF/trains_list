import csv
import numpy as np
from itertools import chain

stations_list = []
matrix = []
pressK = "[!] Press any button to continue..."

def makeStationsList(stations_list):
    with open('test_task_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            try:
                if row['otprSt'] in stations_list:
                    raise Exception()
                stations_list.append(row['otprSt'])
            except:
                pass
    return sorted(stations_list)

def findMinimalPrice(strtStation,finishStation):
    min_price = float;
    min_price = 9999
    
    with open('test_task_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            if row['otprSt'] == strtStation and row['stPrib'] == finishStation:
                if float(row['cost']) < min_price:
                    min_price = float(row['cost'])
                else:
                    pass
    return min_price

def printArray(matrix, stations_list):
    k = 0
    for j in stations_list:
        print('    ',j, end="")
    print(f"\n    ===================================================")
    for i in matrix:
        print(stations_list[k]+"|"+"\t".join(list(map(str, i))))
        k += 1

def createMatrix(station_list, matrix):
    matrix = np.array([ [0]*6 for i in range(6) ], float)
    for i in range(6):
        start = station_list[i]
        for j in range(6):
            end = station_list[j]
            if start == end:
                matrix[i][j] = 0
            else:
                matrix[i][j] = findMinimalPrice(start, end)
    return matrix

def findBestWay(matrix, sl):
    path = []
    counter = 0
    uniq = 0
    minPath = 99999999
    minCounter = 0

    for i1 in range(6):
        for i2 in range(6):
            for i3 in range(6):
                for i4 in range(6):
                    for i5 in range(6):
                        for i6 in range(6):
                            if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i1 != i5) and (i1 != i6) \
                               and (i2 != i3) and (i2 != i4) and (i2 != i5) and (i2 != i6) \
                               and (i3 != i4) and (i3 != i5) and (i3 != i6) \
                               and (i4 != i5) and (i4 != i6) \
                               and (i5 != i6):
                                uniq += 1
                                pth = (f"{sl[i1]} -> {sl[i2]} -> {sl[i3]} -> {sl[i4]} -> {sl[i5]} -> {sl[i6]}")
                                path.append(pth)
                                #print(pth)
                                if matrix[i1][i2] + matrix[i2][i3] + matrix[i3][i4] + matrix[i4][i5] + matrix[i5][i6] < minPath:
                                    minPath = matrix[i1][i2] + matrix[i2][i3] + matrix[i3][i4] + matrix[i4][i5] + matrix[i5][i6]
                                    costLabl = (f"  {matrix[i1][i2]}  {matrix[i2][i3]}  {matrix[i3][i4]}  {matrix[i4][i5]}  {matrix[i5][i6]}")
                                    minCounter = counter
                                counter += 1
    print(f"----------RESULTS----------\nNumber of unique paths: {uniq}")
    print(f"The price of the most advantageous path: {minPath}")
    print(f"-----------PATH------------\n[!] Under each arrow is written the price of the trip!\n\n{path[minCounter]}")
    print(f"{costLabl}\n---------------------------")

#============MAIN=============
print(f"----------CSV INFO----------")
stations_list = makeStationsList(stations_list)
print(stations_list)
print(f"Total amount of stations: {len(stations_list)}\n----------COST TABLE----------\n")

matrix = createMatrix(stations_list, matrix)
printArray(matrix, stations_list)
input(pressK)
findBestWay(matrix, stations_list)

input(pressK)
