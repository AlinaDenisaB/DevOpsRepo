from flask import render_template
from application import app, db, bcrypt
from application.models import Categories, Products
from application.forms import AddCategory, AddProduct

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/products')
def products():
    return render_template('products.html', title='Products')
@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')
@app.route('/admin')
def admin():
    form = AddCategory()
    if form.validate_on_submit():
        category = Categories(category=form.categoryName.data):
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('products'))
    form = AddProducts():
    if form.validate_on_submit():
        product = Products(productName=form.productName.data, productIMG=form.productIMG.data, productInfo=form.productInfo.data, productPrice=form.productPrice.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('admin.html', title="Admin", form=form)
