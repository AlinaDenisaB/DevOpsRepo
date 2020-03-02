from application import db

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryName=db.Column(db.String(30), nullable=False)
    productID=db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'Category ID: ', self.id, '\r\n',
            'Category name: ', self.categoryName, '\r\n'
        ])

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(30), nullable=False)
    productInfo = db.Column(db.String(100), nullable=False)
    productIMG =db.Column(db.LargeBinary, nullable=False)
    productPrice =db.Column(db.Float, nullable=False)
    category = db.relationship('Categories', backref="category", lazy=True)

    def __repr__(self):
        return ''.join(['ProductID: ', str(self.id), '\r\n',
        'ProductName: ', self.productName, '\r\n',
        'ProductInfo: ', self.productInfo, '\r\n',
        'ProductIMG: ', self.productIMG,'\r\n', 'ProductPrice ', self.productPrice
        ])



