from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import psycopg2

# class database_info():
#     database="testdb"
#     user="pgadmin"
#     host="127.0.0.1"
#     password="secure_password"

# c = psycopg2.connect(database=database_info.
#                        database,user=database_info.user,
#                        host=database_info.host,
#                        password=database_info.password)

#https://stackoverflow.com/questions/23839656/sqlalchemy-no-password-supplied-error

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pgadmin:secure_password@localhost:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# notice that all models inherit from SQLAlchemy's db.Model
class Computer(db.Model):

    __tablename__ = "computers" # table name will default to name of the model

    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    memory_in_gb = db.Column(db.Integer)

    # define what each instance or row in the DB will have (id is taken care of for you)
    def __init__(self, name, memory_in_gb):
        self.name = name
        self.memory_in_gb = memory_in_gb

    # this is not essential, but a valuable method to overwrite as this is what we will see when we print out an instance in a REPL.
    def __repr__(self):
        return f"This {self.name} has {self.memory_in_gb} GB of memory"