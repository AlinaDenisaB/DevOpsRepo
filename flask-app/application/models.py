from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name=db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'Category ID: ', self.id, '\r\n',
            'Category name: ', self.category_name, '\r\n'
        ])

class Products(db.Models):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), nullable=False)
    product_info = db.Column(db.String(100), nullable=False)
    product_img =db.Column(db.Longblob, nullable=False)
    product_price =db.Column(db.Float, nullable=False)

    def __repr__(self):
        return ''.join(['ProductID: ', str(self.id), '\r\n',
        'Product name: ', self.product_name], '\r\n',
        'Info: ', self.product_info,'\r\n', 'Price ', self.price
        )



