#IsolatedCoordinateFinder.py
#@author Craig Hutcheon
#referenced https://www.youtube.com/watch?reload=9&v=XqXSGSKc8NU to build algorithm
#@year 2019

#Library Dependencies
import re
import math

#Finds the distance between two points
def distance_between_points(point1, point2):
    x1 = point1[1]
    y1 = point1[2]
    x2 = point2[1]
    y2 = point2[2]

    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

#reads an input text file
def read_text_file(text_file_name):
    #Opens an input text document
    input_file = open(text_file_name, "r")

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

    return coordinates

#Outputs to a text file
def output_text_file(text_file_name, output_coordinate):
    # Opens an output text file
    output_file = open(text_file_name, "w")

    # Writes results to output text file
    Lines = ["--------------\n", "Most Isolated Point\n", "place" + str(output_coordinate[0]) + "\n",
             "--------------\n", "Coordinates\n",
             "(" + str(output_coordinate[1]) + "," + str(output_coordinate[2]) + ")\n",
             "--------------\n", ]
    output_file.writelines(Lines)

    # Closes output file
    output_file.close()

#Creates a two dimensional KDTree from the input dataset
def build_2dtree(points, depth = 0):
    n = len(points)

    if n <=0:
        return None

    #Used to specify what axis to use as pivot of tree
    axis = (depth % 2) + 1

    sorted_points = sorted(points, key = lambda point: point[axis])

    return {
        'point': sorted_points[round(n / 2)],
        'left' : build_2dtree(sorted_points[:round(n /2)], depth + 1),
        'right': build_2dtree(sorted_points[round(n/2) + 1:], depth +1)
    }

#returns the closer point between two points and a pivot
def find_closer_dist(pivot, point1, point2):

    if point1 is None:
        return point2

    if point2 is None:
        return point1

    distance1 = distance_between_points(pivot, point1)

    distance2 = distance_between_points(pivot, point2)

    if distance1 == 0:
        return point2
    elif distance2 == 0:
        return point1
    elif distance1 < distance2:
        return point1
    else:
        return point2

#Used to iterate over tree to find the closest point
def find_closest_point(root, point, depth = 0):
    if root  is None:
        return None
    axis = (depth % 2) + 1

    next_branch = None
    opposite_branch = None

    if point[axis] < root['point'][axis]:
        next_branch = root['left']
        opposite_branch = root['right']

    else:
        next_branch = root['right']
        opposite_branch = root['left']

    best = find_closer_dist(point, find_closest_point(next_branch, point, depth +1), root['point'])

    if distance_between_points(point, best) > abs(point[axis] - root['point'][axis]):
        best = find_closer_dist(point, find_closest_point(opposite_branch, point, depth+1), best)

    return best

#Entry point for algorithm
def find_most_isolated_point():
    #Input for algorithm
    coordinates = read_text_file("problem_big.txt")

    #Builds 2d KDtree
    tree = build_2dtree(coordinates)

    #Initialise Furthest Distance
    furthest_distance = 0

    #Main Comparison Loop
    for coordinate in coordinates:
        closest_coord_dist = distance_between_points(find_closest_point(tree, coordinate), coordinate)

        # if check to determine whether the new result produces a more isolated point
        if closest_coord_dist > furthest_distance:
            furthest_distance = closest_coord_dist
            most_isolated_coordinate = coordinate

        print(coordinate[0])

    #Outputs Result to txt file
    output_text_file("problem_big_output.txt", most_isolated_coordinate)

#Legacy Algorithm that works but is inefficient
def old_algorithm():
    coordinates = read_text_file("problem_small.txt")

    #Initialises furthest distance to its lowest possible number
    furthest_distance = 0

    #compares coordinate with the rest of the coordinates on the array
    for coordinate in coordinates:

        #Set the default distance to max number
        shortest_distance = 10000000

        #compares single coordinate with the other coordinates
        for comparison_coordinates in coordinates:

            #Pythagorean formula for Euclidean distance
            distance = distance_between_points(coordinate, comparison_coordinates)
            # Checks whether the current calculated distance is less than the shortest currently recorded distance
            # Checks whether the distance has been calculated using two identical coordinates
            if (distance < shortest_distance) & (distance != 0):
                shortest_distance = distance
            if (distance < furthest_distance) & (distance != 0):
                break

        #if check to determine whether the new result produces a more isolated point
        if shortest_distance > furthest_distance:
            furthest_distance = shortest_distance
            most_isolated_coordinate = coordinate


        #Prints progress
        print(coordinate[0])

    output_text_file("problem_small_output.txt", most_isolated_coordinate)


