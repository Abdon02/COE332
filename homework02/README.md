# README.md file concerning the files: 'hw02_part1.py' and 'hw02_part2.py'

   The purpose of hw02_part1.py script is to create a dictionary, with data points of meteorite sites. 
   After gathering the data for 5 differnt meteorite sites, I created a JSON file. The JSON file is named
   'meteorite.json' once 'hw02_part1.py' is compiled.

   The purpose of hw02_part2.py script is to read the JSON file that was created from 'hw02_part1.py.
   Given a starting point of the rover, (16.0, 82.0) the rover is instructed to travel to the different 
   meterorite sites based on the order in the JSON file. Depending on the 'composition' of the meteorite
   it would take the rover an (x) amount of time to sample and move on to the next meteorite site. After
   gathering all that time travel from one site to another site, we would calculate the total time it 
   takes for the rover to visit and acquire a sample for each site. 


# 'hw02_part1.py' functions and other information:
### 1.- def element_of_meteorite_composition(mete_comp_list):
     In this function is picks a number between 0 and 2 (inclusive) and depending on what random number
     is chosen. It will return that element from the argument (type list) 'mete_comp_list' to the key 
     value 'composition' for each meteorite site
### 2.- meteorite_dictionary 
     In this directory, it has a key value called, 'sites' that is equal to a list of dictionaries.
     Each dictionary entry has information concering, "site_id", "latitude", "longitude", "composition"
     The value of latitude is randomly generated within the bounds of 16.0 and 18.0. The value of
     longitude is randomly generated within the bounds of 82.0 and 84.0. And the value of composition 
     is determined by the function element_of_meteorite_composition().

# 'hw02_part2.py' functions and other information:
### 1.- def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float):
     This function calculates and returnsthe total distance the rove has to travel from 
     (latitude_1, longitude_1) to (latitude_2, longitude_2).
### 2.- time_to_sample(string_of_key):
     This function will read the key value 'composition' and depending on what the value is stored in 
     that key, it will return either 1, 2, or 3. That interger signifies the amount of time it will 
     take the rover to sample the meteorite
### 3.- get_information(list_of_dict):
     This funtion will return a 2D-matrix that will of size 5x2. It will have 5 rows because each row 
     has information that is needed to solve this problem, which corresponds to a different meteorite 
     landing. The first column of each row will have the total time it takes the rover to travel from 
     one meterorite to another meteorite. The second column of the same row will contain an interger
     that represents how much time it took the rover to gather that data.
### 4.- print_end_results(matrix):
     This function will read the rows of the matrix and create a chart that is similar to what the 
     homework assingment is asking for. In the same function it will sum up the total time it took for 
     the rover to travel from meteorite to meteorite, and gather the sample.