from application import db
from application.models import Categories, Products, categories_products

db.drop_all()
db.create_all()

