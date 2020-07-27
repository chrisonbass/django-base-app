# Python Django Rest Framework
This repo contians a set of services running with `docker-compose`.  The tech stack includes:
  - Python 
    - Django
    - Django Rest Framework
  - nginx 
  - MySQL 
  - React front-end(TODO) 

## Getting Started
### References Used
I used the following sites to piece this together.  
- [Django Project](https://www.djangoproject.com/start/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
### Setup Instructions
First, clone the repo and run the following command
```
docker-compose up --build -d
```

At this point, if you go to `http://localhost:8080/api` in your browser, you will get a gateway error.  We need to run a few commands to get the Django Rest Framework up and running.

  - Connect to the Django container

    ```
    docker exec -it django /bin/bash
    ```

  - Setup the database

    ```
    python manage.py migrate
    ```

  - Create superuser to test api endpoints

    ```
    python manage.py createsuperuser --username admin --email admin@example.com
    ```

  - Finally, start the Django server on port 8000.  

    ```
    python manage.py runserver 0:8000
    ```

    The IP Address and port number need to be written as `0:8000` because Django tries to use the ip address `127.0.0.1` by default.  The server won't be visible to other containers if the 127.0.0.1 ip address is used.


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

## Creating new model/table/api-endpoint
The `manage.py` file in our app root directory is also used to get `apps` started.  We can think of `apps` as a set of files describing models, serializers, and views.
- Create new app

  ```
  python manage.py startapp tasks
  ```
  A new folder labelled `tasks` should be in the app root directory now.

- Modify `tasks/models.py` file
  ```
  from django.db import models

  class Task(models.Model):
      name = models.CharField(max_length=250)
      is_done = models.BooleanField(default=False)
      last_modified = models.DateTimeField(auto_now=True)
  ```
- Create and Modify `tasks/serializers.py`
  ```
  from rest_framework import serializers
  from tasks.models import Task

  class TaskSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model = Task
          fields = ['url', 'name', 'is_done', 'last_modified']
  ```
- Modify `tasks/views.py` file
  ```
  from rest_framework import viewsets
  from tasks.serializers import TaskSerializer
  from tasks.models import Task

  class TaskViewSet(viewsets.ModelViewSet):
      queryset = Task.objects.all()
      serializer_class = TaskSerializer
  ```
- Add new `tasks` app to the base settings file: `basesite/settings.py`
  ```
  INSTALLED_APPS = [
    ...,
    'tasks',
  ]
  ```
- Add `TaskViewSet` API View to the `basesite/urls.py` file
  ```
  from tasks.views import TaskViewSet
  ...
  router.register(r'v1/tasks', TaskViewSet)
  ```  
- Create migration for the new model
  ```
  python manage.py makemigrations
  ```
  Command should output:
  ```
  Migrations for 'tasks':
    tasks/migrations/0001_initial.py
      - Create model Task
  ```
- Execute the migration
  ```
  python manage.py migrate
  ```
  Command should output:
  ```
  Operations to perform:
    Apply all migrations: admin, auth, authtoken, contenttypes, sessions, shift_logs, tasks
  Running migrations:
    Applying tasks.0001_initial... OK
  ```
