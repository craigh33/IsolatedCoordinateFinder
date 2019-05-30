import re
import math

input_file = open("problem_small.txt", "r")

coordinates=[]

#Pulls coordinates from each line of the text document
for line in input_file:
    coordinate = (re.findall('\d+', line ))
    coordinate[1] = int(coordinate[1])
    coordinate[2] = int(coordinate[2])
    coordinates.append(coordinate)

input_file.close()

furthest_distance = 0

#compares coordinate with the rest of the coordinates on the array
for coordinate in coordinates:
    shortest_distance = 999999999999999
    for comparison_coordinates in coordinates:
        distance = math.sqrt(((comparison_coordinates[1]-coordinate[1])**2)+((comparison_coordinates[2]-coordinate[2])**2))
        if (distance < shortest_distance) & (distance != 0):
            shortest_distance = distance
    if shortest_distance > furthest_distance:
        furthest_distance = shortest_distance
        most_isolated_coordinate = coordinate
    print(coordinate[0])

output_file = open("problem_small_output.txt", "w")

Lines = ["--------------\n", "Most Isolated Point\n", "place" + str(most_isolated_coordinate[0]) + "\n", "--------------\n", "Coordinates\n", "(" + str(most_isolated_coordinate[1])+ "," + str(most_isolated_coordinate[2]) + ")\n", "--------------\n",]

output_file.writelines(Lines)

output_file.close()