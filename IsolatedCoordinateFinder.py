import re

file = open("problem_small.txt", "r")

for line in file:
    coordinates = (re.findall('\d+', line ))
    print (coordinates[1])