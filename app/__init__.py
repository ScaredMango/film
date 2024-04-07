from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///film.db'
db = SQLAlchemy(app)

from . import models, views

app.app_context().push()
with app.app_context():
     db.create_all()