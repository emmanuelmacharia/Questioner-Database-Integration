[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![devDependencies Status](https://david-dm.org/liskHQ/lisk-hub/dev-status.svg)](https://david-dm.org/liskHQ/lisk-hub?type=dev)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/emmanuelmacharia/Questioner.svg)

# QUESTIONER #

## Summary ##
Questioner is a web based application that crowd sources the questions people have for a meetup/ event. It helps the organizers of said events or meetups to prioritize questions and enquiries made by the attendees. 

## Technologies ##
- Flask
- Psycopg2
- Postgresql
- Python

## Getting Started ##
- Clone this repository using 
```
git clone https://github.com/emmanuelmacharia/Questioner.git
```

- Navigate to the cloned repository

### Prerequisites ###
1. Python 3 and above
2. Postman
3. Postgres

## Installation ##
- From within the cloned repository directory, create a virtual environment using this command for Linux
    ```
    virtualenv -p python3 venv
    ```  
    or This one for Windows
    ```
    python3 -m venv venv
    ``` 


- Install the dependancies;
    ```
    pip install -r requirements.txt
    ```

- Set up the database [refer here on linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04#creating-a-new-role) or [here](http://www.techken.in/linux/install-postgresql-10-windows-10-linux/) on windows.

- set up a `.env` file where the configurations will be stored. the .env format is as follows: 

    ```
    . venv/Scripts/activate
    export DEBUG=1
    export SECRET_KEY='YourSecretKeyHere'
    export TESTING=True
    export APP_SETTINGS='development'
    export DEVELOPMENT_DATABASE_URL="dbname=dbname user=username password=password"
    export TESTING_DATABASE_URI="dbname=dbname user=username password=password"
    export PRODUCTION_DATABASE_URI="dbname=dbname user=username password=password"
    ```

## Running Tests ##
Run these commands
``` 
pyest
coverage
```
## Testing on Postman ##

- Fire up your development sever by using 
    ```
    python run.py
    ```
- Then on postman, navigate to:
    ```
    localhost:5000/api
    ```

### Note: ###
- You have to create a user first, then sign them in, retreive the token created so that you can access all the other endpoints. These are the only two unrestricted endpoints:

## Unrestricted Endpoints ##

| Endpoints | Functionality |
|-----------|---------------|
|POST/register| Created a user|
|POST/login| Sings the created user in|

## Restricted Endpoints ##
As mentioned, the following endpoints are only accessible to users who sign into the application and have a generated token.
## User Endpoints ##

| Endpoint | Functionality |
| ---------|---------------|
|GET/users | Fetches all the users
|GET/user/email | Fetches a single user by email
|DELETE/user/email | Deletes the specified user
|PUT/user/email| Alters the user properties

## Meetup Endpoints ##

| Endpoint | Functionality |
|----------|---------------|
POST/meetup| Creates a meetup record
GET/meetup/id| fetches a single meetup record by id
GET/meetups| fetches all meetup records
DELETE/meetup/id| Deletes a meetup record
PUT/meetup/id| Alters Meetup record specified

## Question Endpoints ##
| Endpoint | Functionality |
|----------|---------------|
POST/questions | Creates a question
GET/questions | Fetches all questions
GET/question/id | Fetches a single question record by id
DELETE/question/id | Deletes a question by its ID
PUT/question/id | Alters question record

## RSVP Endpoints ##
| Endpoint | Functionality |
|----------|---------------|
POST/rsvp | creates an RSVP record
GET/rsvp | Fetches all rsvp records
GET/rsvp/id | Fetches a single rsvp record by ID
PUT/rsvp | Alters an rsvp record
DELETE/rsvp | deletes an rsvp record by id


## Authors ##

- Emmanuel Macharia *initial work* [emmanuelmacharia](https://github.com/emmanuelmacharia)
- Get in touch on [linkedin](https://linkedin/in/emmanuelmacharia)

## License ##

This project is covered under the MIT License. Read the license in the [LICENSE.md]() file.

## How to Contribute ##
you can fork this repository, and create a Pull Request to the  `branch develop`

