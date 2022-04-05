# Database for the fallen rocks
### _What is this project about?_
---
The purpose of this project is about working with "redis" a database that stores information for an application. While also using Flask to create a flask application that communicates with the database. By creating the following files: **"Dockerfile"**, **"app.py"**, and **"Makefile"** made this project possible. But also using this data file, **"ML_Data_Sample.json"** in order to return various information to the user.

### _Why use a data base?_
---
Previously, I have created a Flask application and containarized the data inside the container. Once the container is stopped and removed, all the data conccerning that application is also thrown away. Hence, the usage of Databases allows us to input and output data to and from the database. So when the flask application is closed, all the data is saved in the database. 

### _How do we use the use database and the flask application_
---
##### **Steps:**
1. You need to pull the following redis image from Dockerhub by doing this command:
    ```
    docker pull redis:6
    ```
2. You then need to run the redis:6 container by doing this command: 
    ```
    docker run -d -p 6436:6379 -v $(pwd)/data:/data:rw --name=<your_name>-redis redis:6 --save 1 1
    ```
    - This line runs the redis:6 contianer is the background and it will gather data very second and will create a copy and write the data and save it inside the folder "data" in your local machine. Inside the data folder there is a file "dump.rdb" that contains all the data.
3. Then you need to acquire the container ID for the redis:6. You can gather that data by doing this command:
    ```
    docker ps -a | grep <your_name>-redis
    ```
4. After acquiring the container ID for the redis:6. You need to acquire the IPAddress that concerns that container, by doing this command:
    ```
    docker inspect <container_id> | grep IPAddress
    ```
5. The IP Address that concerns the redis:6 container will be needed in order to connect the flask application container and the redis:6 container that is currently running.
6. Inside the file "app.py" we will create an object of the class redis. By creating that object inside "app.py" we are able to create this bridge of communication between the flask container and the redis:6 container. Meaning that all the url endpoint command done in the flask application concerning storing and getting data from the redis:6 container is possible. 
    - This is how to create a redis object inside of the flask application
        ```
        rd = redis.Redis(host='IPAdress', port='6379')
        ```
    - The IPAdress is the IPAdress that was acquired in step 4, and the port number is the port number that redis "listens".
### _What are each file about?_
---
- **Dockerfile:**
    - This file contains all the ingredients that are needed for this project. Inside the Dockerfile, it has an OS that will allow me to debug the container if it is neccessary. There is also a copy of the **"ML_Data_Sample.json"** and **"app.py"**. That will have the most up to data code concerning the flask application.
    - Once all the ingredients needed for the flask application it is important to build that Dockerfile to create a Docker Image. We can do that by doing this command:
        ```
        docker build -t abdon02/flask-app:homework05 .
        ```
- **app.py:**
    - This file contains differnet url endpoints that the user can store and return data. This file also "talks" and interacts with the redis:6 container. 
- **Makefile:**
    - This file makes the development and testing process of the flask application much easier.
    - When an edit is made in the file, **"app.py"** it is important to stop and remove the current flask application contianers. Then rebuild the Docker Image, and finally running the flask application container once more. And that process is very easy to do by using a Makefile.
- **ML_Data_Sample.json:**
    - This file is a json file (a dictionary) and inside that dictionary is contains one key and its value is a list of dictionaries. Meaning every element of the list contains a different dictionary that represents information concerining a meteorite landing.
    - In order to download the data into your local computer use this command:
        ```
        wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
        ```
    

### _How to interpret the return information from the flask application?_
---
- It is important that the user started to run the rdeis contianer by following the instructions from above. Then the user needs to run the flask application container by doing this command:
    ```
    docker run --name "abdon-flask" -d -p 5036:5000 abdon02/flask-app:homework05
    ```
- After the redis:6 container and flask application container is running. The user inputs this command:
    ```
    curl -X POST localhost:5036/data
    ```
    - The result is a string message that notifies the user that the data was properly stored inside the database. It looks like this:
        ```
        The data has been uploaded to the redis server, and it has been locally 
        saved in a folder called, "data".
        ```
- After the data has been properly stored in the redis database, the user can do this command to acquire information from the saved data:
    ```
    curl -X GET localhost:5036/data?start=<number>
    ```
    - The <number> is the starting digit index until the very end that will be returned to the user.
        - If the user does not return a valid <number>, meaning if it is a string value or a negative interger value. Then the user will receive this message error:
            ```
            Invalid start value, start must be numeric.
            ```
        - If the user does not input a <number> value or does not include "start=" in the url address then the flask application will return the whole list of dictionaries.
        - If the user does input a valid number to the flask application then a list of dictionaries will be returned. An example will be:
            ```
            [
                {
                    "GeoLocation": "(-75.6691, 60.6936)",
                    "id": "10001",
                    "mass (g)": "5754",
                    "name": "Gerald",
                    "recclass": "H4",
                    "reclat": "-75.6691",
                    "reclong": "60.6936"
                },
                etc...
            ```
### _How to push and pull the flask application from Dockerhub?_
---
- Once the flask application is complete and no more changes are needed to be made. Then to push the docker image to Dockerhub do this command:
    ```
    docker push abdon02/flask-app:homework05
    ```
- In order to pull this image from Dockerhub into your local computer do this command:
    ```
    docker pull abdon02/flask-app:homework05
    ```
