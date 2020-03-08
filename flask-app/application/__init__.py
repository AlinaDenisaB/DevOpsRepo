from flask import Flask, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from os import getenv

app= Flask(__name__)
bcrypt = Bcrypt(app)


app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
app.config['SECRET_KEY'] = str(getenv('MY_SECRET_KEY'))

db = SQLAlchemy(app)

from application import routes
