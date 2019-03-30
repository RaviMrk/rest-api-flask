import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(80))
    caste = db.Column(db.String(80))
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    university = db.Column(db.String(80))
    tfws = db.Column(db.String(80))
    defence = db.Column(db.String(80))
    department = db.Column(db.String(80))



    def __init__(self, username, password, caste, fname, lname, gender, university, tfws, defence, department):
        self.username = username
        self.password = password
        self.caste = caste
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.university = university
        self.tfws = tfws
        self.defence = defence
        self.department = department

    def json(self):
        return {'username': self.username,'password':self.password, 'caste': self.caste, 'fname': self.fname, 'lname': self.lname, 'gender': self.gender, 'university': self.university, 'tfws': self.tfws, 'defence' : self.defence, 'department': self.department }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

