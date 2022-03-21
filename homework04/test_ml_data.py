import pytest
import json 
from ml_data_analysis import compute_average_mass, check_hemisphere, count_classes

#Function that will test the compute_average_mass function
def test_compute_average_mass():
    assert compute_average_mass([{'a': 1}], 'a') == 1
    assert compute_average_mass([{'a' : 1}, {'a': 2}], 'a') == 1.5
    assert compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2
    assert compute_average_mass([{'a': 10}, {'a': 1}, {'a': 1}], 'a') == 4
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True

    #These are test incase invalid things are inputted to the function
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')                      
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')    
    with pytest.raises(ValueError):
        compute_average_mass([{'a': 1}, {'a': 'x'}], 'a')  
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'a': 2}], 'b')    

#Function that will test the check_hemisphere function
def test_check_hemisphere():
    #Makes sure that all the values are printing the correct string
    assert check_hemisphere(1, 1) == 'Northern & Eastern'
    assert check_hemisphere(-1, 1) == 'Southern & Eastern'
    assert check_hemisphere(1, -1) == 'Northern & Western'
    assert check_hemisphere(-1, -1) == 'Southern & Western'

    #Making sure that if the coordinates of (0, 0) are inputted, python is raising an error
    with pytest.raises(ValueError):
        check_hemisphere(0, 0)


#Function that test the count_classes function
def test_count_classes():

    #Test of an empty list of dictionaroes is passed
    with pytest.raises(KeyError):
        count_classes([{}], 'reccclass')

    #Test of an empty list of dictionaries and invalid key
    with pytest.raises(KeyError):
        count_classes([{}], 'r')

    #Test with a random list of dictionaries and a key value
    assert count_classes([{'a' : 1}], 'a') == {1 : 1}
    assert count_classes([{'a' : 2}], 'a') == {2 : 1}
    
    #Test that the results are the same as what are being printed out in the main function
    with open('Meteorite_Landings.json', 'r') as f:
        data = json.load(f)
    
    #Returns the dictionary that will looped through and printout the answer
    dict1 = count_classes(data['meteorite_landings'], 'recclass')
    assert dict1 == {'L5': 1, 'H6': 1, 'EH4': 2, 'Acapulcoite': 1, 'L6': 6, 'LL3-6': 1, 'H5': 3, 'L': 2, 'Diogenite-pm': 1, 'Stone-uncl': 1, 'H4': 2, 'H': 1, 'Iron-IVA': 1, 'CR2-an': 1, 'LL5': 2, 'CI1': 1, 'L/LL4': 1, 'Eucrite-mmict': 1, 'CV3': 1}

    #looping through all the keys of the dictionary and making sure, the values of each key are outputting the correct number 
    for item in dict1:
        if(item == 'L5'):
            assert dict1[item] == 1
        if(item == 'H4'):
            assert dict1[item] == 2
        if(item == 'Iron-IVA'):
            assert dict1[item] == 1
        if(item == 'L6'):
            assert dict1[item] == 6
