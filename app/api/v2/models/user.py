import datetime

from flask import request
from flask_restful import Resource, reqparse
from passlib.hash import pbkdf2_sha256 as sha256

from ..models import dbconnect

conn = dbconnect()
cur = conn.cursor()
class User:
    def __init__(
        self, fullname, password, 
        contact, isadmin = False
        ):
        self.fullname = fullname
        self.contact = contact
        self.isadmin = isadmin
        self.password = password
        self.registered = datetime.datetime.now()

    def firstname(self, fullname):
        return self.fullname.split(' ')[0]

    def lastname(self, fullname):
        return self.fullname.split(' ')[1]

    def othername(self, fullname):
        return self.fullname.split(' ')[-1]

    def email(self, contact):
        return self.contact.split(", ")[0]

    def phonenumber(self, contact):
        return self.contact.split(", ")[-1]

    def username(self, email):
        email = self.contact.split(",")[0]
        return email.split("@")[0]
    #samwelehrmarsha@gmail.com, 254707143761

    def __repr__(self):
        email = self.email(self.contact)
        username = self.username(self.fullname)
        return "<User = {}, email = {}, password = {}>".format(
            username, email, self.password
        )

    def serializer(self):
        firstname = self.firstname(self.fullname)
        lastname = self.lastname(self.fullname)
        othername = self.othername(self.fullname)
        email = self.email(self.contact)
        phonenumber = self.phonenumber(self.contact)
        username = self.username(self.fullname)

        return dict(
            firstname = firstname,
            lastname = lastname,
            othername = othername,
            emial = email,
            phonenumber = phonenumber,
            username = username,
            password = self.password,
            registered = self.registered,
            isadmin = self.isadmin
        )

    def save_user(self):
        '''saves the data in its respective fields'''
        firstname = self.firstname(self.fullname)
        lastname = self.lastname(self.fullname)
        othername = self.othername(self.fullname)
        email = self.email(self.contact)
        phonenumber = self.phonenumber(self.contact)
        username = self.username(self.fullname)

        query = (
            '''INSERT INTO "users"(firstname,lastname,othername,
                    email, username, password, phonenumber, isAdmin, registered)
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', now());'''%
            (firstname, lastname, othername, 
             email, username, self.password, 
             phonenumber, self.isadmin)
        )
        cur.execute(query)
        conn.commit()

    def veiwone(self, email):
        '''finds a single user from the database
            returns a 404 (Not Found) if the user
            doesnt exist'''
        query = "SELECT * FROM users WHERE email = %s;"
        cur.execute(query, (email, ))
        result = cur.fetchone()

        if result is None:
            return False, 404
        else:
            record_format = {
                'id': result[0],
                'firstname': result[1],
                'lastname': result[2],
                'othername': result[3],
                'emial': result[4],
                'username': result[5],
                'password': result[6],
                'phonenumber': result[7],
                'isadmin': result[8],
                'registered': str(result[-1]).split('.')[0]
            }
            return record_format

    def viewall(self):
        '''returns all the records from the database
        if there are no record, the method returns a 
        No record (404)'''
        query = ('SELECT * FROM users')
        cur.execute(query)
        results = cur.fetchall()
        all_records = []
        if results is None:
            return {
                "message": "there are currently no records in \
                    the database",
                "status": 404
            }, 404
        
        for result in results:
            record_format = {
                'id': result[0],
                'firstname' : result[1],
                'lastname' : result[2],
                'othername' : result[3],
                'emial' : result[4],
                'username' : result[5],
                'password' : result[6],
                'phonenumber' : result[7],
                'isadmin' : result[8],
                'registered' : str(result[-1])
            }
            all_records.append(record_format)

        return {
            "message": "user records successfully retreived",
            "users": all_records
        }, 200

    def delete_user(self, email):
        '''deletes the user from the database'''
        exists = User.veiwone(self, email)
        if exists is None:
            return {
                "message": "No user by that email exists",
                "status": 404
                }, 404

        query = "DELETE FROM users WHERE email=%s;"
        cur.execute(query, (email, ))
        conn.commit()
        conn.close()

        return {
            "message":"user deleted successfully",
            "status": 200
        }, 200


    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)    


    
