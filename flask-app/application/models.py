from application import db

class categories(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    categoryName=db.Column(db.String(30), nullable=False, unique=True)
    products=db.relationship('products', backref='categories', lazy=True)
    #productID=db.Column(db.Integer, db.ForeignKey(products.id), nullable=False)
    def __repr__(self):
        return ''.join([
            'CategoryID: ', str(self.id), '\r\n',
            'Category name: ', self.categoryName, '\r\n'
        ])

class products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    productName=db.Column(db.String(30), nullable=False, unique=True)
    productInfo=db.Column(db.String(100), nullable=False, unique=True)
    productIMG=db.Column(db.LargeBinary, nullable=False)
    productPrice=db.Column(db.Float, nullable=False)
    #categories=db.relationship('categories', backref='products', lazy=True)
    categoryID=db.Column(db.Integer, db.ForeignKey(categories.id), nullable=False)
    def __repr__(self):
        return ''.join([
        'Category ID: ', str(self.categoryID), '\r\n',
        'Product ID: ', str(self.id), '\r\n',
        'Product name: ', self.productName, '\r\n',
        'Product info: ', self.productInfo, '\r\n',
        'Product IMG: ', self.productIMG,'\r\n', 'Product price ', self.productPrice
        ])
