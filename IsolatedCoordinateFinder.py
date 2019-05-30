import re
import math

file = open("problem_small.txt", "r")

coordinates=[]

#Pulls coordinates from each line of the text document
for line in file:
    coordinate = (re.findall('\d+', line ))
    coordinate[1] = int(coordinate[1])
    coordinate[2] = int(coordinate[2])
    coordinates.append(coordinate)

furthestdist = 0

#compares coordinate with the rest of the coordinates on the array
for coordinate in coordinates:
    shortestdist= 1000000000
    for comparisoncoord in coordinates:
        dist = math.sqrt(math.pow((comparisoncoord[1]-coordinate[1]),2)+ math.pow((comparisoncoord[2]-coordinate[2]),2))
        if dist != 0:
            if dist < shortestdist:
                shortestdist = dist
    if shortestdist > furthestdist:
        furthestdist = shortestdist
        mostisolatedcoord = coordinate
    print(coordinate[0])



print(furthestdist)
print(mostisolatedcoord)

file.close()