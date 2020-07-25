FROM python:3.8.5

WORKDIR /app

RUN mkdir /baseproject; \
    mkdir /app; \
    python -m pip install Django;\
    python -m pip install djangorestframework;\
    python -m pip install markdown;\
    python -m pip install django-filter;\
    python -m pip install pymysql;\
    cd /baseproject;\
    django-admin startproject basesite;\
    mv -f basesite _basesite;\
    mv -f _basesite/basesite _basesite/manage.py ./;\
    rm -rf _basesite;\
    ls -la /baseproject;

CMD ["/bin/bash","-c","--","while true; do sleep 30; done;"]
# CMD ["python","manage.py","runserver","0:8000"]

# RUN django-admin startproject 
# RUN python manage.py runserver
