# Putting it all together with Kubernetes
---
#### What is this project about?
---
This project is about working with Kubernetes, Redis container, and a Flask API container. From previous homework05 we created a Flask API and created a redis database. From homework05 the user can choose between two http requests: "Get" or "Post". Meaning that the user can store data into the redis database using "Post". And the user can get data returned using "Get". 
In this project we are going to run the Flask API container and the Redis container using kubernetes with the help of Kubernetes.
#### Why should you use Kubernetes 
---
Kubernetes is a portable platform for managing containers. It is a great tool to scale a project if there are many "moving" parts that need to communicate with each other.

#### What are the different "object" types supported by kubernetes?
---
Kubernetes has many object types, but just here are the object types that were used in this project
- 1.- Pods:
    - Pods are the simplest object type that kubernetes supports. If you were to compare it to docker, you can say that a pod is similar to a docker container. A pod can contain many docker containers at the same time, but that is pretty complicated. In this project each pod will be running only one docker container. 
- 2.- Deployments:
    - Deployments are an abstraction and resource type that can be used to run many application components for long periods of time. Inside the deployment declaration, you need to include a pod definition and the number of pod replicas the deployment should be running at all times. Meaning that if the replica number is 2, the deployment will always have 2 replcias of that pod running at all times. If one pod crashed for some reason, the deployment will automatically start a new replica of that pod.  
- 3.- Services:
    - Services are used in order for different components to communicate with other pods over a network. Each pod has its own IP address, and if it were to crash, the deployment will just create a new pod. But by the deployment creating that new copy of the pod, that new pod will have a new IP address. Meaning that the link between the pods would not suffice. Services is great way around that problem.
- 4.- PersistantVolumeClaim (PVC):
    - PVC is an object that is used for the redis container to mount all the data inside the PVC. So incase that redis container crashes the deployment will start a new redis pod with a new IP address, but the PVC will mount itself into that need redis pod containing all the previous information gathered from the previous redis pod. 
#### What are each files used in the Kubernetes about?
---
For this project, I reused the Dockerfile, app.py file from homework05. To add on, I also created the following files that are used in the Kubernetes. 
- 1.- abdon01-test-flask-deployment.yml:
    - This .yml file is the creation of the flask deployment file. Inside this file it pulls the flask-api image from dockerhub that was created and used from homework05 ("abdon02/flask-app:homework05"), and creates two replicas of that pod.  
- 2.- abdon01-test-flask-service.yml:
    - This .yml file connects the flask pods together. Incase a flask pod were to crash, the deployment will start a new flask pod with a new IP address. But with this service, it allows the connection between the pods to be vaid. Since the flask containers run on Flask. Inside this .yml file, it is important to use port 5000 since, that is the port Flask listens to. 
- 3.- abdon01-test-redis-deployment.yml:
    - This .yml file creates the redis deployment file. Inside this file it contiains one replica of the container from the "redis6" image. This is the image that was used in homework05 assingment.
- 4.- abdon01-test-redis-pvc.yml:
    - This .yml file creates creates a PVC object. With this object it mounts the PVC into the redis container. Incase the redis continer were to crash, the data would be saved inside this PVC. The deployment will create a new redis pod and the PVC will be mounted to the new redis container, holding all the previously. 
- 5.- abdon01-test-redis-service.yml:
    - This .yml file creates a service that connects the redis pods together. It is important for the service to be listening to the port number 6379 since that is the port where redis listens to. 
- 6.- pythondebug.yml
    - This .yml file was used to in order to "exec" inside the pod. Once you were inside the pod, you can test the different redis and flask pods to make sure that everything was working.


#### What is inside the "app.py" file and "Dockerfile"?
---
The app.py file contains all the routes that are needed for the user to call. It gives the user two options. 
1.- It allows the user to populate the redis database with data concerning Meteorite_Landings.json file. by using this command:
```
curl -x POST localhost:5000/data    
```
2.- It also allowed the user to get all of the data points from the redis database by using this command: 
```
curl -X GET localhost:5000/data
```
2b.- Or the user had the option to return a specific number and it would return every meteorite landing data starting at that number until the very end. You can use this command:
```
curl -X GET localhost:5000/data?start=<number>
```

Inside the Dockerfile, it has the instructions and ingredients that are needed for the flask container. The flask deployment will be running pods of this flask containers. 
#### How to get results
---
##### Steps:
- 1.- You need to start the redis-pvc pod by doing the command below. By doing so, it will create the PVC mount that willd allow the data to be stored properly incase the redis pod were to crash.
    ```
    kubectl apply -f abdon01-test-redis-pvc.yml
    ```
- 2.- You start the redis deployment by doing the command below. By doing this, the deployment will always have a redis container running. If it were to crash, it would automatically start a new one.
    ```
    kubectl apply -f abdon01-test-redis-deployment.yml
    ```
- 3.- You start the redis service by doing the command below. By doing this it will be incharge of listening to redis on port 6379.
    ```
    kubeclt apply -f abdon01-test-redis-service.yml
    ```
- 4.- You can test to make sure that the redis pods are working porperly by "exec" into the pydebug pod by doing the commands below. The first command is used ot start the pydebug pod. The second command is to see all the pods, services and other kubernetes objects running. By doing that, copy the name of the pydebug pod (the names may vary). The third command allows you to go inside the pydebug pod.
    ```
    kubectl apply -f abdon01-pydebug.yml
    
    kubectl get all
    
    kubectl exec -it py-debug-deployment-5dfcf7bdd9-zzh29 /bin/bash
    ```
    - 4A.- To start testing the redis pods (once inside the pydebug pod) you can populate the redis database by going into a python3 shell and doing the commands below. But first it is important to get the IPaddress of the redis-service.
        ```
        import redis
        
        rd = redis.Redis(host='10.109.122.77', port=6379, db=0)
        
        rd.set("key1": "hello")
        
        rd.get("key1")
        ```
    - 4B.- To make sure the pvc is working delete the current running the redis pod, the redis deployment will start a new one. And then go into the python3 shell and retrive all the data values stored inside the new redis container by doing the commands below. And because of the pvc it should return the correct value that is linked to that key.
        ```
        kubeclt delete pods abdon01-test-deployment-5bfb9c6679-g6l9t
        
        import redis
        
        rd = redis.Redis(host='10.109.122.77', port=6379, db=0)
        
        rd.get("key1")
        ```
- 5.- You start the flask deployment by doing the command below. By doing so the flask deployment will always maintain 2 replicas of the flask containers. 
    ```
    kubectl apply -f abdon01-test-flask-deployment.yml
    ```
- 6.- You start the flask service by doing the command below. By doing so, the flask service will be listening to flask on port 5000.
    ```
    kubectl apply -f abdon01-test-flask-service.yml
    ```
- 7.- You exec into the pydebug pod to start testing the flask containers. TO sucessfully exec into the flask containers use step 4. Then it is important to get the IP address of the flask service by using "kubectl get all" and copying and pasting the IP adress of the flask service.
- 8.- Open up a python3 shell inside the debug pod, and do the following commands to test the flask container below.
    ```
    curl -X POST <IP address of Flask service>:5000/data
    
    curl -X GET <IP address of Flask service>:5000/data
    ```
    - The following will be displayed to the user after the redis database was populated.
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
- 9.- Then you can delete the redis pod and the redis deployment will start a new one. And you can go into the pydebug pod and start a python3 shell. And do the following command to make sure that the data that was stored in the redis database is still inside it.
    ```
    curl -X GET <IP address of Flask service>:5000/data
    ```
    - It should return the exact same result as previously thanks to the redis pvc. 