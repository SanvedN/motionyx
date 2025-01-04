from flask_pymongo import PyMongo
from datetime import datetime

mongo = PyMongo()

def init_db(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/motionyz"
    mongo.init_app(app)

# mongo.connect('your_database')

def get_patient_schema():
    return {
        "name": str,
        "age": int,
        "dob" : datetime,
        "email": str,
        "password": str,
        "gender"  :str,
        "medicalHistory": list,  
        "currentSymptoms": list 
    }

def get_therapist_schema():
    return {
        "name": str,
        "age": int,
        "dob" : datetime,
        "email": str,
        "password": str,
        "gender"  :str,
        "qualification" : str,
        "expertise" : str, # I'm looking at you, Namita Thapar 
        "YearOfExperience" : str
    }