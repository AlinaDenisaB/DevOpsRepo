from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import categories, products
from application.forms import CategoryForm, ProductForm
import flask_bcrypt

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/products')
def products():
    #productsData=products.query.all()
    return render_template('products.html', title='products')
#, products=productsData)
@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    session=db.session
    categoryForm = CategoryForm()
    if categoryForm.validate_on_submit():
        categories = categories(category=categoryForm.categoryName.data)
        db.session.add(categories)
        db.session.commit()
        return redirect(url_for('products'))
    productForm = ProductForm()
    if productForm.validate_on_submit():
        products = products(productName=productForm.productName.data, productIMG=productForm.productIMG.data, productInfo=productForm.productInfo.data, productPrice=productForm.productPrice.data)
        db.session.add(products)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('admin.html', title="Admin", categoryForm=categoryForm, productForm=productForm)

