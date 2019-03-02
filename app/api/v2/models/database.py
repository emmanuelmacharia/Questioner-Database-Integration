#database.py
# CONTAINS QUERIES FOR CREATING THE TABLES IN THE DATABASE

query1 = """CREATE TABLE IF NOT EXIST user(id serial PRIMARY KEY,
                                           firstname text NOT NULL,
                                           lastname text NOT NULL, 
                                           othername text NOT NULL,
                                           email text NOT NULL UNIQUE,
                                           phonenumber text NOT NULL UNIQUE,
                                           username text NOT NULL,
                                           isAdmin bool NOT NULL,
                                           password text NOT NULL,
                                           registered TIMESTAMP NOT NULL);"""

query2 = """CREATE TABLE IF NOT EXIST meetup(id serial PRIMARY KEY,
                                             createdOn TIMESTAMP NOT NULL,
                                             location text NOT NULL,
                                             topic text NOT NULL,
                                             happeningOn DATE NOT NULL,
                                             tags text NOT NULL);"""


query3 = """CREATE TABLE IF NOT EXIST question(id serial PRIMARY KEY,
                                               createdOn TIMESTAMP NOT NULL,
                                               createdBy INTEGER REFERENCES user(id),
                                               meetup INTEGER REFERENCES meetup(id),
                                               title text NOT NULL,
                                               body text NOT NULL,
                                               votes INTEGER NOT NULL);"""
        
query4 = """CREATE TABLE IF NOT EXIST rsvp(id serial PRIMARY KEY,
                                           user INTEGER REFERENCES user(id),
                                           meetup INTEGER REFERENCES meetup(id),
                                           response text NOT NULL,
                                           date_confirmed TIMESTAMP NOT NULL);"""

deleteuser = "DROP TABLE user;"
deletemeetup = "DROP TABLE meetup;"
deletequestion = "DROP TABLE question;"
deletersvp = "DROP TABLE rsvp;"

# nonduplicate = "CREATE EXTENSION IF NOT EXISTS citext" #prevents duplication of meetup events
# alter = "ALTER TABLE meetup ALTER COLUMN topic TYPE citext"

queries = [query1, query2, query3, query4]
deleters = [deleteuser, deletersvp, deletemeetup, deletequestion]