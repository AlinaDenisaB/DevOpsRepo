from flask import render_template
from application import app

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
    return render_template('admin.html', title="Admin")
