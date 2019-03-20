#database.py
# CONTAINS QUERIES FOR CREATING THE TABLES IN THE DATABASE

query1 = """CREATE TABLE IF NOT EXISTS "users"(id serial PRIMARY KEY,
                                           firstname text NOT NULL,
                                           lastname text NOT NULL, 
                                           othername text NOT NULL,
                                           email text NOT NULL UNIQUE,
                                           username text NOT NULL,
                                           password text NOT NULL,
                                           phonenumber text NOT NULL UNIQUE,
                                           isAdmin bool NOT NULL,
                                           registered TIMESTAMP NOT NULL);"""

query2 = """CREATE TABLE IF NOT EXISTS "meetup"(id serial PRIMARY KEY,
                                             createdOn TIMESTAMP NOT NULL,
                                             location text NOT NULL,
                                             topic text NOT NULL,
                                             happeningOn DATE NOT NULL,
                                             tags text NOT NULL);"""


query3 = """CREATE TABLE IF NOT EXISTS "question"(id serial PRIMARY KEY,
                                               createdOn TIMESTAMP NOT NULL,
                                               createdBy INTEGER REFERENCES "users"(id),
                                               meetup INTEGER REFERENCES "meetup"(id),
                                               title text NOT NULL,
                                               body text NOT NULL,
                                               votes INTEGER NOT NULL);"""
        
query4 = """CREATE TABLE IF NOT EXISTS "rsvp"(id serial PRIMARY KEY,
                                           "user" INTEGER REFERENCES "users"(id),
                                           meetup INTEGER REFERENCES "meetup"(id),
                                           response text NOT NULL,
                                           date_confirmed TIMESTAMP NOT NULL);"""

deleteuser = "DROP TABLE \"users\" CASCADE;"
deletemeetup = "DROP TABLE \"meetup\" CASCADE;"
deletequestion = "DROP TABLE \"question\" CASCADE;"
deletersvp = "DROP TABLE \"rsvp\" CASCADE;"

adminquery = (
    '''INSERT INTO "users" (
                    firstname,lastname,othername,
                    email, username, password, phonenumber, isAdmin, registered
                    )
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', now());''' %
    ('emmanuel', 'marsha', 'c', 'marshac@cruithne.com', 'marsha11', 'Permafrost1', '06549392', True)
)
# nonduplicate = "CREATE EXTENSION IF NOT EXISTS citext" #prevents duplication of meetup events
# alter = "ALTER TABLE meetup ALTER COLUMN topic TYPE citext"

queries = [query1, query2, query3, query4]
deleters = [deleteuser, deletersvp, deletemeetup, deletequestion]
