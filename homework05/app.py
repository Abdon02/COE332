from flask import Flask, jsonify, request
import json
import redis
from typing import List

app = Flask(__name__)

#Function that has one route that handels both a POST and a GET request
@app.route('/data', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def load_meteorite_landings_data() -> str:
    '''
    This function will put Meteorite_landings_data into the redia server, or it will return the json
    file to the user.

    Args:
        None

    Returns:
        (string) it will return a string telling the user what task has been done, or if an error was
        committed and therefore it needs to be fixed.
    '''
    #Creating an object of redis
    rd = redis.Redis(host ='172.17.0.21', port='6379', db = 0)    
    
    if(request.method == 'POST'):
        #This variable will have the json file
        data = read_json_file()

        #This is creating a redis object, make sure the host number is correct

        rd.set("Meteorite_landings", json.dumps(data))
        return """
        \nThe data has been uploaded to the redis server, and it has been locally saved in a folder
        called, "data".\n
        """
    elif(request.method == 'GET'):
        #If the rd variable empty, and they did a get before post then we return an error message
        if(rd.keys() == []):
            return '''
            \nYou need to first make a post, since there is no data stored in the server. Therefore,
            do this command first:
            
            curl -X POST localhost:5036/data 

            then you can redo this GET command without any issues.\n
            '''
        else:
            #Querys the the start value from the URL address
            start = request.args.get('start', 0)
            
            #Change the value of start to str
            start = str(start)
            
            if (start == None):
                return 'Make sure you input a value after "start" or make sure you included "start" in the URL'
            
            #Checks if the value inputted is a number
            if not start.isnumeric():
               return 'Invalid start value, start must be numeric.\n'

            #Converting the starting value to a int number
            start = int(start)
            
            #The database has information concerning the json data, and 'd' is a dictionary
            d = json.loads(rd.get('Meteorite_landings'))

            #Return the dictoany with the starting point
            return jsonify(d['meteorite_landings'][start:]) 

    #Incase the user inputs another method that isn't what is offered
    else:
        return ''' 
        You inputted the incorrect method option. You are only allowed to use GET and POST http verbs
        for this function. Try again but instead you these commands:
        1.- If you want to upload the data into the data base use this:
            curl -X POST localhost:5036/data 

        2.- If you want to read the data out of the database and return it as a json list use this 
        command:
            curl -X GET localhost:5036/data
        '''

#Function that will open the json file
def read_json_file():
    with open('ML_Data_Sample.json', 'r') as f:
        data = json.load(f)

        return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
