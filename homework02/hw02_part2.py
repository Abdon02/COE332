import json
import math

mars_radius = 3389.5  #km

#This function will calculate the time it takes to travel from one meteorite to another meteorite
def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

#function will print out the end result, as shown in hw02 assingment
def print_end_results(matrix):
    #counter for the print message and sum to find total time
    i = 0
    sum = 0

    for row in matrix:
        i = i + 1
        print('leg = ', i, 'time to travel = ', round(row[0], 2), 'hr, time to sample = ', round(row[1], 2), "hr")
        sum = sum + row[0] + row[1]
        

    print('===============================')
    print("number of legs = ", i, "total time elapsed = ", round(sum,2), "hr")

#function that will determine how long it will take to get sample at each site, return an interger
def time_to_sample(string_of_key):
    if(string_of_key == 'stony'):
        return 1
    elif(string_of_key == 'iron'):
        return 2
    else:
        return 3

#function will calculate all the information and store it in a 2D matrix
def get_information(name_of_dict):
    matrix_2d = []
    row_info = []
    starting_coordinates = [16.0, 82.0]

    for row in name_of_dict['sites']:        
        distance = calc_gcd(starting_coordinates[0], starting_coordinates[1], float(row['latitude']), float(row['longitude']))
        row_info.append(distance / 10) #This is the total hours it took to travel the inputted 'distance'
        row_info.append(time_to_sample(row['composition']))
        matrix_2d.append(row_info)
        row_info = []
        starting_coordinates[0], starting_coordinates[1] = row['latitude'], row['longitude']
        
    return matrix_2d
        

#We are going to read the json file 
with open('meteorite.json', 'r') as filein:
    meteorite_data = json.load(filein)

matrix = get_information(meteorite_data)

print_end_results(matrix)
