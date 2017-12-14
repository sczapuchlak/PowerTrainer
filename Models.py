from app import app
from flask_sqlalchemy import SQLAlchemy

# creating SQLAlchemy database
database = SQLAlchemy(app)

# User Model class, sets up database columns and metadata
class User(database.Model):
    user_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    username = database.Column(database.String(50), nullable=False, unique=True)
    password = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(50), nullable=False)

# constructor method
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


    def __repr__(self):
        return '<User: %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)


# Item Model class and constructor
class Exercise(database.Model):
    exercise_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    exercise_name = database.Column(database.String(50), nullable=False)
    exercise_weight = database.Column(database.String(20),nullable=False)
    exercise_reps = database.Column(database.String(50),nullable=False)

    def __init__(self,exercise_name,exercise_weight,exercise_reps):
        self.exercise_name = exercise_name
        self.exercise_weight= exercise_weight
        self.exercise_reps = exercise_reps

    def __repr__(self):
        return '<Exercise: %r>' % self.exercise_name,self.exercise_weight,self.exercise_reps


