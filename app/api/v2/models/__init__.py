'''creates a connection with the databases'''
import os
import psycopg2
from .database import queries, deleters, adminquery

environment = os.getenv('APP_SETTINGS')
development_url = os.getenv('DEVELOPMENT_DATABASE_URI')
testing_url = os.getenv('TESTING_DATABASE_URI')
production_url = os.getenv('PRODUCTION_DATABASE_URI')

def dbconnect():
    '''connects to the databases'''
    # try:
    '''try connecting to one of the three environments set'''
    if environment == 'testing':
        connection = psycopg2.connect(
            "postgresql://marsha11:Permafrost@localhost:5432/questionert"
            )
    if environment == 'production':
        connection = psycopg2.connect(
            "postgresql://marsha11:Permafrost@localhost:5432/questionerpr"
            )
    if environment == 'development':
        connection = psycopg2.connect(
            "postgresql://marsha11:Permafrost@localhost:5432/questionerdev"
            )
    # except Exception as e:
    #     print (e, "No connection")
    print(connection)
    return connection


conn = dbconnect()
print(conn)

def create_tables():
    '''creates the tables in our database that
    would store all user information. 
    this function will be called when the
    application is first run'''
    conn = dbconnect()
    cur = conn.cursor()

    for query in queries:
        cur.execute(query)
    conn.commit()
    cur.close()

def drop_tables():
    '''deletes tables
    this function is important for testing purposes
    where the dummy data is deleted when the tests 
    finish running
    '''
    testconn = dbconnect()
    cur = testconn.cursor()
    for query in deleters:
        cur.execute(query)


def create_admin():
    '''creates an admin user'''
    conn = dbconnect()
    cur = conn.cursor()
    cur.execute(adminquery)
    conn.commit()
    cur.close()

def check_admin():
    '''checks if an admin already exists'''
    conn = dbconnect()
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id ='%s';" % (1, )
    cur.execute(query)
    admin = cur.fetchone()
    if admin is None:
        return create_admin()
    else:
        pass

        


