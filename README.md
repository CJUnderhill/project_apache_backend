# projectapache
This repository contains the backend REST API of the APACHE project, which aims to help in 
collecting and analyzing noise complaints from inner-city Copenhagen.

This project is built with Django and the Django REST Framework.

### Setup
This section details the steps required to set this project up.

##### Requirements
The APACHE backend system has the following dependencies:

- Python 3.*
  - Django 2.*
  - djangorestframework 3.7.7+
  - Pillow 5.*
  - pytz 2018.3+
- virtualenv
  
Ensure that the proper version of python is installed before proceeding.

##### Configuration
This section assumes the you are operating in a bash terminal.

First, enter the `apache` directory in the main project folder. Create a virtual environment for this project by running:
```
virtualenv -p python3 venv
```

Then activate this virtual environment by running:
```
source venv/bim/activate
```
This will isolate the operations of this program from the rest of the operating system.
Finally, install all of the python dependencies listed above. You may run this command to do so:
```
pip install Django djangorestframework Pillow pytz
```

##### Instantiate the database
We now have to create and set up the server's database. To do so, run the following commands:
```
python3 manage.py makemigrations api
python3 manage.py migrate
```

If you encounter any errors, try deleting the `migrations` folder in the `api` directory
and the `db.sqlite3` file in the main directory, then re-run the two commands above.

##### Create a super user
The API requires that you have account access before you are allowed to interact with it. To create an account,
simply run the following code and follow the prompts:
```
python3 manage.py createsuperuser
```

### Run the server
You may run the server with the following command:
```
python3 manage.py runserver
```

This will open an endpoint at [http://localhost:8000/complaints/](http://localhost:8000/complaints/).
You can navigate to this endpoint in your browser to try the API, or interact with it in any other way you see fit.
