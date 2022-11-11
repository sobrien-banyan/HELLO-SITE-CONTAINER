# HELLO-SITE-CONTAINER

## To start app run the following:
in root directory
1. install venv run `python3 -m venv venv`
2. activate venv run `source venv/bin/activate` or `. venv/bin/activate`
3. to start server in HELLO-SITE-CONTAINER/hello_site `python3 manage.py runserver`




## useful stuff during build

Django steps

1. Create virtual environment  ->      ‘python3 -m venv venv’
2. Activate it  ->   source venv/bin/activate
3. Install Django ‘pip install django’
4. Create a django project with ‘Django-admin startproject <project-name>’
5. Run ‘python3 manage.py runserver’ to see if it worded. -> install Django in the app  ` ‘pip install django’`
6. Create an ‘app’ inside your project with ‘python manage.py startapp <app-name>’
7. Install your new app in your projects setting file
8. Follow the steps
    1. URL —— home
    2. Data to send back. <- ‘hello’
    3. Logic to connect them HelloWorldView



To add requirements in root run the following command 
pip3 freeze > requirements.txt