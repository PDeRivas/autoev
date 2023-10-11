import os

from flask import Flask
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

from app.models.models import(
    app,
    Usuario,
    Pais,
    Provincia,
    Localidad
)

load_dotenv()