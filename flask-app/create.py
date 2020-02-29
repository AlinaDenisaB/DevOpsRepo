from application import db
from application.models import Categories, Products

db.drop_all()
db.create_all()

