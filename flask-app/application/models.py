from application import db

class Categories(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    categoryName=db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return ''.join([
            'CategoryID: ', str(self.id), '\r\n',
            'CategoryName: ', self.categoryName, '\r\n'
        ])

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    productName=db.Column(db.String(50), nullable=False)
    productInfo=db.Column(db.String(100), nullable=False)
    productIMG=db.Column(db.String(50), nullable=False)
    productPrice=db.Column(db.Float, nullable=False)
    def __repr__(self):
        return ''.join([
        'ProductID: ', str(self.id), '\r\n',
        'ProductName: ', self.productName, '\r\n',
        'ProductInfo: ', self.productInfo, '\r\n',
        'ProductIMG: ', self.productIMG,'\r\n', 
        'ProductPrice ', self.productPrice 
        ])
class categories_products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    categoryID=db.Column(db.Integer, db.ForeignKey(Categories.id), nullable=False)
    productID=db.Column(db.Integer, db.ForeignKey(Products.id), nullable=False)
