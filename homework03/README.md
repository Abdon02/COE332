# Water samples of Mars

  Before I start talking about 'hw03_part2.py' and 'test_hw03_part3.py' it is important that we download the JSON
  file that contains the water data. This data will be used in to find the turbidity and the time it will take
  for the water to be in the "safe" level for water consumption.

#### To download the JSON file follow these steps:
  ___
  ```
  1.- Go to the directory where you want this file to be

  2.- copy and paste this into your terminal:

  wget https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

  *The data get updated every day, so the results may vary when it is time to make calculations*
  ```
The purpose of 'hw03_part2.py' is to calculate the average Turbidity of the water from the last 5 recent recordings To calculate the Turbidity, you use this formula, T= a0 * I90, where T is Turbidity, a0 is the Calibration Constant, I90 is the Ninety degree dectector. To calculate the turbidity we will use the function 'calculate_turbidity()' where it will return a floating number.

There is a turbidity threshold, meaning that if the calculated turbidity is over the threshold it is not safe to use that water. If the turbidity is less than or equal to the Turbidity Threshold, then it is safe to use. We will use the function 'is_water_safe_to_drink()', where it will return a bool value, and will determine if it is safe or not to use the water.

If the turbidity makes the water unsafe to use, then we calculate the amount of time (hours) it will take to bring the turbdity level under the threshold, using the function 'required_time_for_turbidity_to_go_under_threshold()'. The function will return a floating number that represents the time it will take for the water to go under the threshold. The formula to calculate the time is the following: Ts > T0(1-d)**b, where Ts is the turbidity threshold, T0 is the current turbidity level, d is the decay rate per hour, and b is time (in hours). 

The purpose of 'test_hw03_part2.py' is to test the functions that were created in the script, 'hw03_part2.py'.
By importing the functions, json, and pytest we are able to create and different functions to test the functions
from 'hw03_part2.py'. The goal was to create 5 different tests for each function that contested the answer returned
 and cases where errors would be raised. I created, 'test_calculate_turbidity()' where it tests the function,
'calculate_turbidity()'. I created, 'test_is_water_safe()' where it tests the function 'is_water_safe()'. Finally,
I created a function 'test_time()' where it tests the function, 'required_time_for_turbidity_to_go_under_threshold()'. 



# 'hw03_part2.py' functions and other information:
___
### 1.- def calculate_turbidity(list_of_dict, cali_key, detc_cur_key, num_of_recordings):
The argument list_of_dicts is the value of the key for the dictionary, gathered from the JSON file. The JSON file 
is then read in the main function. The argument cali_key is a string argument that will be used to get the value of
calibration for each dictionary. Finally, the argument num_of_recordings is an int value that signifies how many 
recent data points, it wants to analyze in order to calculate the Turbidity. The reason a list of dictionaries was 
pass so we didn't have to pass the whole dictionary. 

### 2.- def is_water_safe_to_drink(turb):
The argument turb is the current turbidity of the water. If the turbidity is greater than 1.0 then it is not safe to
drink the water, and it returns False. If the current turbidity is less thatn or equal to 1.0 then it is safe to 
drink the water, and it retruns True. The result of this function will either alert the user a warning message 
saying that the water should not be consumed. If the function returns a value of True, then it will alert the user
that the water is safe to drink using an info message. 

### 3.- def required_time_for_turbidity_to_go_under_threshold(current_turb):
The argument current_turb is the turbidity, and using the equation, Ts > T0(1 - d)**b, we are able to find b.
In order to find b, we are need to use logs, therefore we will need to import math in order to use the method
math.log() to calculate b.

# 'test_hw03_part3.py' functions and other information:
___ 
### 1.- def test_calculate_turbidity():
This function opens the 'turbidity_data.json' file that was downloaded. And it passes a list of dictionaries, 
the calibration key, and the dectector key, num_of_recent_recordings, into the function, 'calculate_turbidity()'. 
And in this function, I was checking that the value that was returning was correct, or incorrect by changing the 
argument for num_of_recent_recordings. Also tested to make sure that the function was returning a float number. 
Finally tested the cases where an empty list was inputted, an incorrect key was inputtd, and when an argument was 
missing when the function was called. 

### 2.- def test_is_water_safe():
This function tests to make sure that the function 'is_water_safe()' returns a boolean value. It also tested 
different scenarios with different turbidity readings. Finally, it tested when the argument was not inputted as a 
floating number, and raised an error

### 3.- def test_time():
This function tests to make sure that the return value from the function 'required_time_for_turbidity_to_go_under_threshold()', is a floating number. It also tests the hours returned from the function for differt turbidity readings.
Finally, it tests what would happen if a string argument was passed into the function instead of a flaoting number.