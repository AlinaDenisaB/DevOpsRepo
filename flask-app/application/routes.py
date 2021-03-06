from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import Categories, Products, categories_products
from application.forms import CategoryForm, ProductForm, UpdateProducts, DeleteProduct
import flask_bcrypt
import os
import secrets
from werkzeug.utils import secure_filename
from PIL import Image

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/products')
def products():
    products = Products.query.all()
    categories=Categories.query.all()
    loc_image= url_for('static', filename='productIMG/')
    return render_template("products.html", categories=categories, products=products, loc_image=loc_image)

@app.route('/cart')
def cart():

    return render_template("cart.html", title='Cart')

def save_img(form_picture):
    random_hex = secrets.token_hex(8)
    _name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/productIMG', picture_fn)
    output_size=(300,250)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

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
        if productForm.productIMG.data:
            FinalIMG=save_img(productForm.productIMG.data)
            Products.productIMG = FinalIMG

        product=Products(
                productName=productForm.productName.data, 
                productInfo=productForm.productInfo.data,
                productIMG=FinalIMG,
                productPrice=productForm.productPrice.data
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))
    
    updateProduct=UpdateProducts()
    if updateProduct.validate_on_submit():
        newPrice=Products.query.filter_by(productName=updateProduct.productName.data).update(dict(productPrice=updateProduct.productPrice.data))
        db.session.commit()
        return redirect(url_for('products'))

    deleteProduct=DeleteProduct()
    if deleteProduct.validate_on_submit():
        Products.query.filter_by(productName=deleteProduct.productName.data).delete()
        db.session.commit()
        return redirect(url_for('products'))

    return render_template('admin.html', form=categoryForm, form1=productForm, form2=updateProduct, form3=deleteProduct)
