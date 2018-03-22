# APACHE Project Backend
This repository contains the backend REST API of the APACHE project, which aims to help in 
collecting and analyzing noise complaints from inner-city Copenhagen.

This project is built with Django and the Django REST Framework.

## Setup
This section details the steps required to set this project up.

### Requirements
The APACHE backend system has the following dependencies:

- Python 3.*
  - Django 2.*
  - djangorestframework 3.7.7+
  - Pillow 5.*
  - django-cors-headers 2.2.*
  - virtualenv 15.0.1+
  - django-filter 1.1.*
  - djangorestframework-filters 0.10.2+
  
Ensure that the proper version of python is installed before proceeding.

### Configuration
This section assumes the you are operating in a bash terminal.

First, enter the main project folder. Create a virtual environment for this project by running:
```bash
pip3 install virtualenv
virtualenv -p python3 venv
```

Then activate this virtual environment by running:
```bash
source venv/bin/activate
```
This will isolate the operations of this program from the rest of the operating system.
Finally, install all of the python dependencies listed above. You may run this command to do so:
```bash
pip3 install Django djangorestframework django-cors-headers django-filter djangorestframework-filters Pillow
```

### Instantiate the database
We now have to create and set up the server's database. To do so, run the following commands:
```bash
python3 manage.py makemigrations api
python3 manage.py migrate
```

If you encounter any errors, try deleting the `migrations` folder in the `api` directory
and the `db.sqlite3` file in the main directory, then re-run the two commands above.

### Create a super user
The API requires that you have account access before you are allowed to interact with it. To create an account,
simply run the following code and follow the prompts:
```bash
python3 manage.py createsuperuser
```

## Run the server
You may run the server with the following command:
```bash
python3 manage.py runserver
```

This will open an endpoint at [http://localhost:8000/complaints/](http://localhost:8000/complaints/).
You can navigate to this endpoint in your browser to try the API, or interact with it in any other way you see fit.

## API Reference
The API is accessible through the following endpoints:

### Get Authentication Token

Send the user's login information to receive a system-generated authentication token.

**URL** : `/get-token/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints**

The username and password of the account.

```json
{
    "username": "[unicode 64 chars max]",
    "password": "[unicode 64 chars max]"
}
```

**Data example** All fields must be sent.

```json
{
    "username": "root",
    "password": "icebrent"
}
```

#### Success Response

**Code** : `200 OK`

**Content examples**

The authentication token for a valid user.

```json
{
    "token": "1415ac00daa2d25d177990e457e373810d138a47"
}
```

### Send a complaint to the system

Get a list of every complaint in the system.

**URL** : `/complaints/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Headers**

The authentication token associated with the account.

```
    "Authorization": "Token [System-generated Authentication Token]"
```

**Header example** All fields must be sent.

```
    "Authorization": "Token 3e98cec2d1280100c8c4ea65e0eaaf0b2b384674"
```

**Data constraints**

The information contained within the complaint.

```json
{
    "comments": "[String 250 characters max]",
    "severity": "[Integer between 1 and 5]",
    "latitude": "[Float]",
    "longitude": "[Float]",
    "image": "[NOT REQUIRED; Local file location unicode 128 characters max]",
    "audio": "[NOT REQUIRED; Local file location unicode 128 characters max]"
}
```

**Data example**

```json
{
    "comments": "Street Noise",
    "severity": 5,
    "latitude": 55.1,
    "longitude": 11.5,
    "image": "C:/media/photos/2018-03-15_151316.1207580000.jpg"
}
```

#### Success Response

**Code** : `201 CREATED`

**Content examples**

A list of JSON objects containing all complaints within the system.

```json
{
    "id": 1,
    "timestamp": "2018-03-15T15:13:16.120758Z",
    "owner": "root",
    "comments": "Street Noise",
    "severity": 5,
    "latitude": 55.1,
    "longitude": 11.5,
    "image": "http://localhost:8000/media/photos/2018-03-15_151316.1207580000.jpg",
    "audio": null
}
```

### Get List of Complaints in System

Get a list of every complaint in the system.

**URL** : `/complaints/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Headers**

The authentication token associated with the account.

```
    "Authorization": "Token [System-generated Authentication Token]"
```

**Header example** All fields must be sent.

```
    "Authorization": "Token 3e98cec2d1280100c8c4ea65e0eaaf0b2b384674"
```

#### Success Response

**Code** : `200 OK`

**Content examples**

A list of JSON objects containing all complaints within the system.

```json
[
    {
        "id": 1,
        "timestamp": "2018-03-15T15:13:16.120758Z",
        "owner": "root",
        "comments": "Street Noise",
        "severity": "5",
        "latitude": 55.1,
        "longitude": 11.5,
        "image": "http://localhost:8000/media/photos/2018-03-15_151316.1207580000.jpg",
        "audio": "http://localhost:8000/media/audio/2018-03-15_151316.1207580000.aac"
    }
]
```

### Get an Individual Complaint (by ID)

Get an individual complaint from within the system using the complaint's ID.

**URL** : `/complaints/:pk/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Headers**

The authentication token associated with the account.

```
    "Authorization": "Token [System-generated Authentication Token]"
```

**Header example** All fields must be sent.

```
    "Authorization": "Token 3e98cec2d1280100c8c4ea65e0eaaf0b2b384674"
```

#### Success Response

**Code** : `200 OK`

**Content examples**

A single JSON object containing a queried complaint from within the system.

```json
{
    "id": 6,
    "timestamp": "2018-03-15T15:13:16.120758Z",
    "owner": "root",
    "comments": "Street Noise",
    "severity": "5",
    "latitude": 55.1,
    "longitude": 11.5,
    "image": "http://localhost:8000/media/photos/2018-03-15_151316.1207580000.jpg",
    "audio": "http://localhost:8000/media/audio/2018-03-15_151316.1207580000.aac"
}
```

### Create a user account

Create a user account in the system.

**URL** : `/users/`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Headers**

The authentication token associated with the posting account.

```
    "Authorization": "Token [System-generated Authentication Token]"
```

**Header example** All fields must be sent.

```
    "Authorization": "Token 3e98cec2d1280100c8c4ea65e0eaaf0b2b384674"
```

**Data constraints**

Required user account information.

```json
{
    "username": "[String 30 characters max]",
    "password": "[String 6 characters min]",
    "first_name": "[Unicode 64 characters max]",
    "last_name": "[Unicode 64 characters max]"
}
```

**Data example**

```json
{
    "username": "chadju",
    "password": "testpassword",
    "first_name": "Chad",
    "last_name": "Underhill"
}
```

#### Success Response

**Code** : `201 CREATED`

**Content examples**

A JSON object containing the new user's data.

```json
{
    "username": "chadju",
    "password": "testpassword",
    "first_name": "Chad",
    "last_name": "Underhill",
    "complaints": []
}
```

### Get List of Users in System

Get a list of every user in the system.

**URL** : `/users/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Headers**

The authentication token associated with the account.

```
    "Authorization": "Token [System-generated Authentication Token]"
```

**Header example** All fields must be sent.

```
    "Authorization": "Token 3e98cec2d1280100c8c4ea65e0eaaf0b2b384674"
```

#### Success Response

**Code** : `200 OK`

**Content examples**

A list of JSON objects containing all users within the system.

```json
[
    {
        "id": 1,
        "username": "root",
        "complaints": [
            1,
            2,
            3,
            4
        ]
    }
]
```

### Get an Individual User (by ID)

Get an individual user from within the system using the user's ID.

**URL** : `/users/:pk/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Headers**

The authentication token associated with the account.

```
    "Authorization": "Token [System-generated Authentication Token]"
```

**Header example** All fields must be sent.

```
    "Authorization": "Token 3e98cec2d1280100c8c4ea65e0eaaf0b2b384674"
```

#### Success Response

**Code** : `200 OK`

**Content examples**

A single JSON object containing a queried user from within the system.

```json
{
    "id": 1,
    "username": "root",
    "complaints": [
        1,
        2,
        3,
        4
    ]
}
```

### Filter complaints

Filter complaints by a number of criteria.

**URL** : `/complaints/?owner=&severity=&category=&timestamp_0=&timestamp_1=&latitude_0=&latitude_1=&longitude_0=&longitude_1=`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Headers**

The authentication token associated with the account.

```
    "Authorization": "Token [System-generated Authentication Token]"
```

**Header example** All fields must be sent.

```
    "Authorization": "Token 3e98cec2d1280100c8c4ea65e0eaaf0b2b384674"
```

#### Available Filters

**Owner** : `/complaints/?owner=<userID>`

**Severity** : `/complaints/?severity=<integer>`

**Category** : `/complaints/?category=<String>`

**DateTime Range** : `/complaints/?timestamp_0=<ISO8601_DateTime>&timestamp_1=<ISO8601_DateTime>`

**Latitude Range** : `/complaints/?latitude_0=<float>&latitude_1=<float>`

**Longitude Range** : `/complaints/?longitude_0=<float>&longitude_1=<float>`

#### Usage Example

Selecting complaints from user with ID of 1, where severity was listed as 5 and category was "music":

`/complaints/?owner=1&severity=5&category=music`

Selecting complaints between 1:15pm and 1:20pm on March 15th, 2018:

`/complaints/?timestamp_0=2018-03-15+13:15:00&timestamp_1=2018-03-15+13:20:00`

Selecting complaints between latitude ranges of 55.1 and 55.1 and longitude ranges of 11.4 and 11.6:

`/complaints/?latitude_0=55.1&latitude_1=55.2&longitude_0=11.4&longitude_1=11.6`


#### Success Response

**Code** : `200 OK`

**Content examples**

A list of JSON objects containing all complaints within the system that fit the configured filters.

```json
[
    {
        "id": 1,
        "timestamp": "2018-03-15T15:13:16.120758Z",
        "owner": "root",
        "comments": "Street Noise",
        "severity": "5",
        "latitude": 55.1,
        "longitude": 11.5,
        "image": "http://localhost:8000/media/photos/2018-03-15_151316.1207580000.jpg",
        "audio": "http://localhost:8000/media/audio/2018-03-15_151316.1207580000.aac"
    }
]
```
