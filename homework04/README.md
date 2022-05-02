# __Working with containers__

### __What's this project about?__
This project is about working with containers, by using the follwoing files: "__ml_data_analysis.py__", "__Meteorite_Landings.json__", "__test_ml_data.py__". I created a Docker Image called, "__abdon02/ml_data_analysis:hw04__" that had the ability to run and execute the files from above. This README file will tell you about it.

### __What are each file about?__
- __ml_data_analysis.py__: 
    - This file reads the "__Meteorite_Landings.json__" file and summarizes the data. The file calculates the Average mass of 30 meterors, counts how many meteorites landed in the 4 different hemisphere quadrants. And counts the amount of times each class was brought up. This an example of the output:
        ```
        Summary data following meteorite analysis:

        Average mass of 30 meteor(s):
        83857.3 grams

        Hemisphere summary data:
        There were 21 meteors found in the Northern & Eastern quadrant
        ... etc
        
        Class summary data:
        The L5 class was found 1 times
        The H6 class was found 1 times
        ... etc
        ```
    
- __Meteorite_Landings.json__:
    - This JSON file is a list of dictionaries, each element of the list is a different dictionary. Each dictionary is information concerning a different Meteorite Landing. The following is an example of one meteorite landing information:
        ```
        {
            "meteorite_landings": [
            {
            "name": "Ruiz",
            "id": "10001",
            "recclass": "L5",
            "mass (g)": "21",
            "reclat": "50.775",
            "reclong": "6.08333",
            "GeoLocation": "(50.775, 6.08333)"
            }, 
            ... etc 
        }
        ```
    - You can pull this json file from the internet using this command:
        ```
        wget https://raw.githubusercontent.com/tacc/coe-332-sp22/main/docs/unit04/scripts/Meteorite_Landings.json
        ```
        
- __test_ml_data.py__:
    - This file contains unit tests concerning file "__ml_data_analysis.py__". When running the tests the output should look like this if all tests were passed:
        ```
        ========================================= test session starts =======================================
        platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
        rootdir: /home/abdon01/COE332/COE332/homework04
        collected 3 items

        test_ml_data.py ...                                                                         [100%]

        ========================================== 3 passed in 0.01s ========================================
        ```
        

## __How was the Docker image built?__
The Docker Image, was built with the help of a Dockerfile. The Dockerfile contains instructions and ingredients that are going to be needed to in order to finally built the Docker Image. 

- The following "ingredients" were used in the Dockerfile: 
    ```
    Operating system: Centos 7.9

    Dependencies:
        Python3 
        Pytest 7.0.0
    
    Files that were copied:
        ml_data_analysis.py
        Meteorite_Landings.json
        test_ml_data.py
    ```
- After including all the ingredients for the Dockerfile, I used the following command to build the Dockerfile into a Docker Image, with a tag "hw04": 
    ```
    docker build -t abdon02/ml_data_analysis:hw04 .
    ```
- To push the Docker Image to Docker Hub, use this command:
    ```
    docker login
    ... etc

    docker push abdon02/ml_data_analysis:hw04
    ```

### __How to pull and use the Docker Image " _abdon02/ml_data_anaylysis:hw04_ " from Docker Hub?__

- To pull the image from Docker Hub copy and paste the following code in your terminal:
    ```
    docker pull abdon02/ml_data_analysis:hw04
    ```
- To run the Docker Image interactively use these commands:
    ```
    docker run --rm -it abdon02/ml_data_analysis:hw04 /bin/bash
    ```
    - To run the "__ml_data_analysis.py__" file use this command (with the json file that is inside the container):
        ```
        ./ml_data_analysis.py Meteorite_Landings.json
        ```
    - To run the "__test_ml_data_analysis.py__" file use this command:
        ```
        pytest
        ```
- To run the Docker Image interactively with a user-provided data set found in the web use these commands:
    - To download the data set from the internet use this command:
        ```
        wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json 
        ```
    - After downloading the data set, use this command to copy the data set into the folder "code" that is inside the container:
        ```
        docker run --rm -it -v $PWD:/code abdon02/ml_data_ananlysis:hw04 /bin/bash
        ```
    - Then you run and execute the ml_data_analysis.py file using the user-defined data using this command:
        ```
        ./ml_data_analysis.py ML_Data_Sample.json
        ```

