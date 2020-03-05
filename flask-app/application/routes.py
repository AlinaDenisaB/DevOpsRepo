from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Categories, Products, categories_products
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
    categoryForm=CategoryForm()
    if categoryForm.validate_on_submit():
        category=Categories(
                categoryName=categoryForm.categoryName.data
            )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('products'))
    
    productForm=ProductForm()
    if productForm.validate_on_submit():
        product=Products(
                productName=productForm.productName.data,
                productInfo=productForm.productInfo.data,
                productIMG=productForm.productIMG.data,
                productPrice=productForm.productPrice.data
            )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('admin.html', form=categoryForm, form1=productForm)

