import os

from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
 
from sqlalchemy import ForeignKey

app = Flask(__name__)  


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@ip/nombre_db
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    es_admin = db.Column(db.Boolean, nullable=False)

class Pais(db.Model):
    __tablename__ = 'pais'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)

class Provincia(db.Model):
    __tablename__ = 'provincia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    pais_id = db.Column(db.Integer, ForeignKey('pais.id'), nullable=False)

class Localidad(db.Model):
    __tablename__ = 'localidad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    provincia_id = db.Column(db.Integer, ForeignKey('provincia.id'), nullable=False)
