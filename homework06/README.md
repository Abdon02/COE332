# Putting it all together with Kubernetes
---
#### What is this project about?
---
This project is about working with Kubernetes, Redis container, and a Flask API container. From previous homework05 we had to create a Flask API and create a redis datbase. From homework05 the user can choose between two http requests: "Get" or "Post". Meaning that the user can store data into the redis database using "Post". And the user can get dat returned using "Get". 
In this project we are going to run the Flask API contianer and the Redis container using kubernetes.
#### Why should you use Kubernetes 
---
Kubernetes ia portable platform for managingin containers. It is a great tool to scale a project if there are many "moving" parts that need to communicate with each other

#### What the different "object" types supported by kubernetes?
---
Kubernetes has many object types, but just here are the object types that were used in this project
- 1.- Pods:
    - Pods are the simplest object type that kubernetes supports. If you were to compare it to docker, you can say that a pod is similar to a docker container. A pod can contain many docker containers at the same time, but that is pretty complicated. In this project each pod will be running only one docker container
- 2.- Deployments:
    - Deployments are an abstraction and reource type that can be used to run many applciation components for long periods of time. Inside the deployment declaration, you need to include a pod definitio and the number of replicas the deployment should be running at all times. Meaning that if the replica number is 2, that means the that deployment will always have 2 replcias of that pod running at all times. If one pod crashed for some reason, the deployment will automatically start a new replica of that pod.
- 3.- Services:
    - Services are used in order for different components to communicate wiht each other over a network to other pods. Each pod has its own IP address, and if it were to crash, the deployment will just create a new pod. But by the deployment creating that new instance of the pod, that new pod has a new IP adress. Meaning that the link between the pods would not suffice. Services is great way around that problem.
- 4.- PersistantVolumeClaim (PVC):
    - PVC is an object that is used for the redis container to mount all the data inside the PVC. So incase that redis container crashes the deployment will start a new redis pod with a new IP address, but the PVC will mount itself into that need redis pod containing all the previous information gathered from the previous redis pod. 
#### What are each files about?
---
For this project, I reused the Dockerfile, app.py file from homework05. To add on, I also created the following files that are used in the Kubernetes. 
- 1.- abdon01-test-flask-deployment.yml:
    - This .yml file is the creation of the flask deployment file. Inside this file it pull the flask-api image from dockerhub that was created and used from homework05, and creates two replicas of that pod. 
- 2.- abdon01-test-flask-service.yml:
    - This .yml file connects the flask pods together. Incase a flask pod were to crash, the deployment will start a new flask pod with a new IP address. But with this service, it allows the connection between the pods to be vaid.
- 3.- abdon01-test-redis-deployment.yml:
    - This .yml file creates the redis deployment file. Iside this file it contiains one replica of the container from the "redis6" image. 
- 4.- abdon01-test-redis-pvc.yml:
    - This .yml file creates creates a PVC object. With this object it mounts the PVC into the redis container. Incase the redis continer were to crash, that would be saved inside this PVC. The deployment will create a new redis pod and the PVC will be mounted to the new redis contianer, holding all the saved data previously set. 
- 5.- abdon01-test-redis-service.yml:
    - This .yml file creates a service that connects the pods together in order for the new and existing pods acn communicate with each other. 
- 6.- pythondebug.yml
    - This .yml file was used to in order to "exec" inside the pod. Once you were inside the pod, you could test that the data that was saved inside one redis pod was infact saved. And if you were to delete that current redis pod, the redis deployment would automatically start a new one. And using the same debugpython pod, you could test that the data was correct.
    - You could also use this pythongdebug pod in order to curl the requests to make sure that the flask containers were working. In order to use the curl, we had to use the IP of the flask service. Since the service connected the flask pods together.
#### How to get results
---
##### Steps:
- 1.- You need to get the IP address of the flask service. You can do that by doing this command:
    ```
    kubectl get services
    ```
    A list of all the services will show up. Get the IP address of the Flask Service.
- 2.- You need to exec into the pythondebug by doing this command:
    ```
    kubectl exec -it <debugpython> /bin/bash
    ```
    Once you do this command you will be inside the pythondebug container.
- 3.- You can start to curl commands from inside the pythondebug container by this command:
    ```
    curl <IP-address-of-flask-service>:5000/data
    ```
    And the result will be this:
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
    