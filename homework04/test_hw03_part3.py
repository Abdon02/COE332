import pytest
import json
from hw03_part2 import calculate_turbidity, is_water_safe_to_drink, required_time_for_turbidity_to_go_under_threshold


#Testing the calculate_turbidity function
def test_calculate_turbidty():
    with open ('turbidity_data.json', 'r') as file:
        data = json.load(file)

    #Test that we are getting the correct turbidity value, for the last 5 recent recordings
    assert calculate_turbidity(data['turbidity_data'], 'calibration_constant', 'detector_current', 5) == 1.14975

    #Test that we are getting the correct turbidity value for the last 6 recent recordings
    assert calculate_turbidity(data['turbidity_data'], 'calibration_constant', 'detector_current', 6) == 1.14903

    #Test that the function is returning a float, for the last 5 recent recordings
    assert isinstance(calculate_turbidity(data['turbidity_data'], 'calibration_constant', 'detector_current', 5), float) == True

    #Test when an empty list is passed in.
    with pytest.raises(IndexError):
        calculate_turbidity([], 'calibration_constant', 'dectector_current', 5)

    #Test when you input the wrong list key value
    with pytest.raises(KeyError):
        calculate_turbidity(data['data'], 'calibration_constant', 'dectector_current', 5)

    #Test when you forget to input an argument to the function, in this case, the number of recent recordings is missing
    with pytest.raises(TypeError):
        calculate_turbidity(data['turbidity_data'], 'calibration_constant', 'dectector_current')
    
    
#Testing the is_water_safe_to_drink function
def test_is_water_safe():
    
    #Test that the return value of this function is a bool type
    assert isinstance(is_water_safe_to_drink(1.0), bool) == True

    #Test the return value is True
    assert is_water_safe_to_drink(.9) == True

    #Test the return value is False
    assert is_water_safe_to_drink(1.9) == False

    #Test the return value is True, when the turbidity is the value of the threshold
    assert is_water_safe_to_drink(1.0) == True

    #Test when the argument is not a number
    with pytest.raises(TypeError):
        is_water_safe_to_drink('1.999')

    
#Testing the required_time_for_turbidity_to_go_under_threshold function
def test_time():

    #Test how much time it will take for turbidity to go under the threshold
    assert required_time_for_turbidity_to_go_under_threshold(1.14903) == 6.88

    #Test how much time it will take for turbidity to go under the threshold 
    assert required_time_for_turbidity_to_go_under_threshold(1.14975) == 6.91

    #Test that the function returns a float number
    assert isinstance(required_time_for_turbidity_to_go_under_threshold(1.14903), float) == True
    
    #Test when the inputted argument is not a floating number
    with pytest.raises(TypeError):
        required_time_for_turbidity_to_go_under_threshold('1.14903')

    #Test how much time it will take for turbidity to under the threshold when the turbidity is at the threshold
    assert required_time_for_turbidity_to_go_under_threshold(1.) == 0.
    
