import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    cast = db.Column(db.String(80))
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    university = db.Column(db.String(80))
    tfws = db.Column(db.String(80))
    defence = db.Column(db.String(80))
    department = db.Column(db.String(80))



    def __init__(self, email, password, cast, fname, lname, gender, university, tfws, defence, department):
        self.email = email
        self.password = password
        self.cast = cast
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.university = university
        self.tfws = tfws
        self.defence = defence
        self.department = department

    def json(self):
        return {'email': self.email,'password':self.password, 'cast': self.cast, 'fname': self.fname, 'lname': self.lname, 'gender': self.gender, 'university': self.university, 'tfws': self.tfws, 'defence' : self.defence, 'department': self.department }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

