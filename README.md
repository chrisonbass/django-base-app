# Python Django Rest Framework
This repo contians a set of services running with `docker-compose`.  The tech stack includes:
  - Python 
    - Django
    - Django Rest Framework
  - nginx 
  - MySQL 
  - React front-end(TODO) 


## Getting Started
First, clone the repo and run the following command
```
docker-compose up --build -d
```

At this point, if you go to `http://localhost:8080/api` in your browser, you will get a gateway error.  We need to run a few commands to get the Django Rest Framework up and running.

  - First, let's get connect to the Django container

    ```
    docker exec -it django /bin/bash
    ```

  - Then, we need to setup of the data base

    ```
    python manage.py migrate
    ```

  - To login and test commands, we'll need to create a super user

    ```
    python manage.py createsuperuser --username admin --email admin@example.com
    ```

  - Finally, we start the Django server on port 8000.  

    ```
    python manage.py runserver 0:8000
    ```

    We have to write the ip and port as `0:8000` because Django tries to use the ip address `127.0.0.1` by default.  Which isn't visible to other containers in the docker-compose configuration.


## File Notes
Please note that files that were not modified during setup were left out from the notes below
```
# docker build scripts
docker/
  django/
    Dockerfile 

# docker volume mount
vol/            
  django/
    basesite/   # root configuration
      settings.py      # Where middleware is loaded, database configured, etc
      urls.py          # This is where the url endpoints are mapped
    shift_logs/ # custom app endpoint
      models.py        # Contains model classes for custom endpoint
      serializers.py   # Serializers convert models to native Python data types
      views.py         # Parses http GET, POST, DELETE, etc requests using a model and serializer
    manage.py   # django command line script
    mysql.cnf   # mysql config used by django to connect to mysql container
```

## Creating new table/endpoint
