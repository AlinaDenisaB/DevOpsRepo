from application import db

class categories(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    categoryName=db.Column(db.String(30), nullable=False)
    products=db.relationship('products', backref='categories', lazy=True)
    #productID=db.Column(db.Integer, db.ForeignKey(products.id), nullable=False)
    def __repr__(self):
        return ''.join([
            'CategoryID: ', str(self.id), '\r\n',
            'CategoryName: ', self.categoryName, '\r\n'
        ])

class products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    productName=db.Column(db.String(50), nullable=False)
    productInfo=db.Column(db.String(100), nullable=False)
    productIMG=db.Column(db.LargeBinary, nullable=False)
    productPrice=db.Column(db.Float, nullable=False)
    #categories=db.relationship('categories', backref='products', lazy=True)
    categoryID=db.Column(db.Integer, db.ForeignKey(categories.id), nullable=False)
    def __repr__(self):
        return ''.join([
        'ProductID: ', str(self.id), '\r\n',
        'ProductName: ', self.productName, '\r\n',
        'ProductInfo: ', self.productInfo, '\r\n',
        'ProductIMG: ', self.productIMG,'\r\n', 
        'ProductPrice ', self.productPrice, '\r\n',
        'CategoryID:', str(self.categoryID)
        ])
