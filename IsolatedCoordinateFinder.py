#IsolatedCoordinateFinder.py
#@author Craig Hutcheon
#@year 2019

#Library Dependencies
import re
import math

#Opens an input text document
input_file = open("problem_big.txt", "r")

#Initialises an array to store coordinate data
coordinates=[]

#Pulls coordinates from each line of the text document
for line in input_file:
    coordinate = (re.findall('\d+', line ))
    coordinate[1] = int(coordinate[1])
    coordinate[2] = int(coordinate[2])
    coordinates.append(coordinate)

#Closes input text document
input_file.close()

#Initialises furthest distance to its lowest possible number
furthest_distance = 0

#compares coordinate with the rest of the coordinates on the array
for coordinate in coordinates:

    #Set the default distance to max number
    shortest_distance = 10000000

    #compares single coordinate with the other coordinates
    for comparison_coordinates in coordinates:#

        #Pythagorean formula for Euclidean distance
        distance = math.sqrt(((comparison_coordinates[1]-coordinate[1])**2)+((comparison_coordinates[2]-coordinate[2])**2))

        #Checks whether the current calculated distance is less than the shortest currently recorded distance
        #Checks whether the distance has been calculated using two identical coordinates
        if (distance < shortest_distance) & (distance != 0):
            shortest_distance = distance

    #if check to determine whether the new result produces a more isolated point
    if shortest_distance > furthest_distance:
        furthest_distance = shortest_distance
        most_isolated_coordinate = coordinate

    #Prints progress
    print(coordinate[0])

#Opens an output text file
output_file = open("problem_big_output.txt", "w")

#Writes results to output text file
Lines = ["--------------\n", "Most Isolated Point\n", "place" + str(most_isolated_coordinate[0]) + "\n", "--------------\n", "Coordinates\n", "(" + str(most_isolated_coordinate[1])+ "," + str(most_isolated_coordinate[2]) + ")\n", "--------------\n",]
output_file.writelines(Lines)

#Closes output file
output_file.close()