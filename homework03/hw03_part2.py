import json
import logging
import math
from typing import List

#Setting for logging
logging.basicConfig(level = logging.DEBUG)

#Global variable, turbidity threshold
NTU = 1.0

#Global variable, decay factor
DECAY_FACTOR = 0.02

#Function that will calculate the turbidity using 'equation 1'
def calculate_turbidity(list_of_dict: List[dict], cali_key: str, detc_cur_key: str, num_of_recent_recordings: int) -> float:
    """
    This function will calculate the turbidity using equation 1. It will gather data from the five 
    most recent data points.

    Args:
        list_of_dictionaries (list): A list of dictionaries, each element of the list corresponds to
                                     a different dictionary. We have to turn the value of that key
                                     into a floating number.
        calibration_key (str): This is a string that will be used to get the data from the dicts.
                               This is the "key" value. We have to turn the value of that key value 
                               into a floating number.
        dectector_current_key (str): This is a string that will be used to get the data from the 
                                     dictionaries. This is the "key" value.
        num_of_recent_recordings (int): This a int value that signifies how many recent dat points
                                        does it want to analyze to calculate the Turbidity
    Returns: 
        turbidity (float): The avaerage turbidity values from the last 5 recent data points
    """
    
    #sum of turbidity, turbidity = calibration * detector current
    turb = 0
    count = 0

    #For loop to gather the data from the list of dictionaries
    for i in range(1, num_of_recent_recordings + 1):
        count = count + 1
        turb = turb + float(list_of_dict[-i][cali_key]) * float(list_of_dict[-i][detc_cur_key])    
    
    return round(turb / count, 5)

#Function will return if the water is safe to drink or not
def is_water_safe_to_drink(turb):
    """
    This function will see if the water is safe to drink or not

    Args:
        turb (float): It is the current turbidity gathered from the list of dictionaries

    Returns:
        result (bool): It returns True or False if the water is safe to drink (True) or if the water 
                       should be avoided (False)
    """

    if(turb <= NTU):
        return True

    return False


#Function that will calculate the minimum time to fall below threshold using equation 2
#If it is below the safe threshold, it will return '0'
def required_time_for_turbidity_to_go_under_threshold(current_tur):
    """
    This function will determine the amount of time it will take to get the current_turbidity to go 
    under the allowable threshold.

    Args:
        current_tur (float): It is the current turbidity reading 

    Returns:
        time (float): The amount of hours it will take for the water to go under the threshold

    """
    if(current_tur <= NTU):
        return 0

    return round((math.log(NTU / current_tur))/ (math.log(1 - DECAY_FACTOR)), 2)


#This is the main function that will call the other functions
def main():
    #This will read the json file and set the data into a varaiable
    with open('turbidity_data.json', 'r') as read_file:
        turbidity_data = json.load(read_file)

    num_of_recent_recordings = 5
    tur = calculate_turbidity(turbidity_data['turbidity_data'], 'calibration_constant', 'detector_current', num_of_recent_recordings)

    #Prints the average turbidity 
    print("Average turbidity based on the most recent", num_of_recent_recordings, "measurements =", tur, "NTU") 

    #It decides wether it is safe to drink the water or not
    is_it_safe_to_drink = is_water_safe_to_drink(tur)

    if(is_it_safe_to_drink == True):
        logging.info("Turbidity is below threshold for safe use")
    else:
        logging.warning("Turbidity is above threshold for safe use")

    #It calculates the minimum time required ot return below a safe threshold
    time = required_time_for_turbidity_to_go_under_threshold(tur)
    print("Minimum time required to return below a safe threshold =", time, "hours")

#Calling the main function
if __name__ == "__main__":
    main()
