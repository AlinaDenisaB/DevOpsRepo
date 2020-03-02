from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from os import getenv

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://alina:password@localhost/db"
app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes
