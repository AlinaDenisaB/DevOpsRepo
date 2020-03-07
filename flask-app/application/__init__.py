from flask import Flask, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from os import getenv

app= Flask(__name__)
bcrypt = Bcrypt(app)


#app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://alina:password@127.0.0.1/db"
app.config['SECRET_KEY']="zxcvbnmpoiuytlkjhfdsgjvd"
#app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))

db = SQLAlchemy(app)

from application import routes
