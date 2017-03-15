from flask import Flask
from app import db
#from app import app
import datetime

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(255))
    password = db.Column(db.String(255))
    datecreated = db.Column(db.DateTime)

    def __init__(self,firstname,lastname,username,gender,age,bio,password,datecreated):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.gender = gender
        self.age = age
        self.bio = bio
        self.password = password
        self.datecreated=datecreated
    def __repr__(self):
        return '<name %r>' % self.firstname


    
