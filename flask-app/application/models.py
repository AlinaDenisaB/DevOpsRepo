from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryName=db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'Category ID: ', self.id, '\r\n',
            'Category name: ', self.categoryName, '\r\n'
        ])

class Products(db.Models):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(30), nullable=False)
    productInfo = db.Column(db.String(100), nullable=False)
    productIMG =db.Column(db.LargeBinary, nullable=False)
    productPrice =db.Column(db.Float, nullable=False)

    def __repr__(self):
        return ''.join(['ProductID: ', str(self.id), '\r\n',
        'Product name: ', self.productName], '\r\n',
        'Product info: ', self.productInfo], '\r\n',
        'ProductIMG: ', self.productIMG,'\r\n', 'Product price ', self.productPrice
        )



