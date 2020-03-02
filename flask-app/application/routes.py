from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Categories, Products
from application.forms import CategoryForm, ProductForm
import flask_bcrypt

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
@app.route('/products')
def products():
    productsData=Products.query.all()
    return render_template('products.html', title='Products', products=productsData)
@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    category_form = CategoryForm()
    if category_form.validate_on_submit():
        category = Categories(category=category_form.categoryName.data)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('products.html'))
    product_form = ProductForm()
    if product_form.validate_on_submit():
        product = Products(productName=product_form.productName.data, productIMG=product_form.productIMG.data, productInfo=product_form.productInfo.data, productPrice=product_form.productPrice.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products.html'))
    return render_template('admin.html', title="Admin", category_form=category_form, product_form=product_form)
