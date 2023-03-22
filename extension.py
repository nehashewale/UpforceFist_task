import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:ns30@localhost:5432/demo1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)