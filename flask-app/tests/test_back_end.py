import unittest
import pytest_check as check

from flask import abort, url_for, redirect
from flask_testing import TestCase

from application import app, db
from application.models import Categories, Products

class TestBase(TestCase):

    def create_app(self):
        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
                SQLALCHEMY_DATABASE_URI='mysql+pymysql://alina:password@127.0.0.1/dbtest')
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test product
        testProduct = Products(productName="nameTEST", productInfo="This is a test product", productIMG="test.jpg", productPrice="10")

        # create test category
        testCategory = Categories(categoryName="cattest")

        # save the product and the category to database
        db.session.add(testProduct)
        db.session.add(testCategory)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        """
        Test if the home page is accesible
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_productspage_view(self):
        """
        Test if the products page is accesible
        """
        response = self.client.get(url_for('products'))
        self.assertEqual(response.status_code, 200)

    def test_cartpage_view(self):
        """
        Test if the products page is accesible
        """
        response = self.client.get(url_for('cart'))
        self.assertEqual(response.status_code, 200)

    def test_adminpage_view(self):
        """
        Test if the admin page is accesible
        """
        response = self.client.get(url_for('admin'))
        self.assertEqual(response.status_code, 200)

class testForms(TestBase):

    def test_addProducts(self):
        """
        Test if the products are added to the database correctly
        """
        #create a test product
        testProduct=Products()

        #set the attributes
        testProduct.productName='nameTEST'
        testProduct.productInfo='This is a test product'
        testProduct.productIMG='test.jpg'
        testProduct.productPrice='10'

        #save it 
        db.session.add(testProduct)

        #check if it's in the database
        all_products=Products.query.all()
        #self.assertEqual(len(all_products), 1)
        only_product=all_products[1]
        self.assertEqual(only_product, testProduct)

        #check attributes
        self.assertEqual(only_product.productName, 'nameTEST')
        self.assertEqual(only_product.productInfo, 'This is a test product')
        self.assertEqual(only_product.productIMG, 'test.jpg')
        self.assertEqual(only_product.productPrice, '10')

    def test_addCategory(self):
        """
        Test if the categories can be added
        """
        testCategory=Categories()
        testCategory.categoryName="cattest"
        db.session.add(testCategory)
        all_categories=Categories.query.all()
        #self.assertEquals(len(all_categories), 1)
        only_category=all_categories[1]
        self.assertEqual(only_category, testCategory)
        self.assertEqual(only_category.categoryName, 'cattest')

    def test_create(self):
        assert self.client.get('/admin').status_code == 200
        self.client.post('/admin', data={'title': 'created', 'body': ''})

        with app.app_context():
            count = db.session.execute('SELECT COUNT(id) FROM products').fetchone()[0]
            assert count == 1

    def test_updateProductPrice(self):
        """
        Test if the price of the products can be updated
        """
        testProduct=Products.query.filter_by(productName='nameTEST').first()
        self.assertTrue(testProduct)
        assert testProduct.productPrice != '10'

    def test_update(self):
        assert self.client.get('/admin').status_code == 200
        self.client.post('/admin', data={'productPrice': 'updated', 'body': ''})

        with app.app_context():
            up = db.session.execute('SELECT * FROM products WHERE id=1').fetchone()
            assert up['productPrice']==10.0 

    def test_deleteProduct(self):
        """
        Test if the products can be deleted
        """
        testDelProd=Products.query.filter_by(productName='nameTEST').delete()
        self.assertTrue(testDelProd)
    
    def test_delete(self):
        response=self.client.post('admin')

        with app.app_context():
            product = db.session.execute('SELECT * FROM products WHERE id=2').fetchone()
            assert product is None

    def create_test_img():
        file=BytesIO()
        image=Image.new('RGBA', size=(300,250), color=(155,0,0))
        image.save(file, 'png')
        file.name='test.png'
        file.seek(0)
        return file
        form=response.forms['form_picture']
        form['picture_fn']=('picture_fn', create_test_img().read())
        form.submit()

class testValidators(TestBase):
    def testLenght(self):
        x=len('nameTEST')
        a=1
        b=100
        c=range(2,101)
        d=102
        check.greater(x,a)
        check.less_equal(x, b)
        check.is_in(x, c, "Lenght ok")
        check.is_not_in(d, c, "Lenght not ok")

    def validate_input(self):
        responde = self.client.post('/admin', data={'productName' : 'nameTEST', 'productInfo':'This is a test product', 'productIMG':'test.jpg', 'productPrice':'10'})
        assert message in response.data


