# README.md file concerns the files: 'hw03_part2.py' and 'test_hw03_part3.py'

  Before I start talking about 'hw03_part2.py' and 'test_hw03_part3.py' it is important that we download the JSON
  file that contains the water data. This data will be used in to find the turbidity and the time it will take
  for the water to be in the "safe" level for water consumption.

#### To download the JSON file follow these steps:
  ___
  1.- Go to the directory where you want this file to be

  2.- copy and paste this into your terminal:

  wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

  *The data get updated every day, so the results may vary when it is time to make calculations*

  
The purpose of 'hw03_part2.py' is to calculate the average Turbidity of the water from the last 5 recent recordings To calculate the Turbidity, you use this formula, T= a0 * I90, where T is Turbidity, a0 is Calibration Constant, I90is the Ninety degree dectector. To calculate the turbidity we will use hte function 'calculate_turbidity()' where it will return a float number.

There is a turbidity threshold, meaning that if the turbidity that was calculated is over the threshold it is not safe to drink that water. If the turbidity is less than or equal to the Turbidity Threshold, then it is safe to consume. We will use the function 'is_water_safe_to_drink()', where it will return a bool value.

If the turbidity makes the water unsafe to consume, then we calculate the amount of time (hours) it will take to bring the turbdity level under the threshold, using the function 'required_time_for_turbidity_to_go_under_threshold()'. That will return a float number.

# 'hw03_part2.py' functions and other information:
### 1.- def calculate_turbidity(list_of_dict, cali_key, detc_cur_key, num_of_recordings):
The argument list_of_dicts is the value of the key for the dictionary, gathered from the JSON file. The JSON file 
is then read in the main function. The argument cali_key is a string argument that will be used to get the value of
calibration for each dictionary. Finally, the argument num_of_recordings is an int value that signifies how many 
recent data points, it wants to analyze in order to calculate the Turbidity. 

