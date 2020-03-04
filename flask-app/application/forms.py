from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import categories, products

class CategoryForm(FlaskForm):
    categoryName = StringField('CategoryName',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    submit=SubmitField('Add category!')

class ProductForm(FlaskForm):
    productName = StringField('ProductName',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    productInfo = StringField('ProductInfo',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    productIMG = FileField('ProductIMG',
        validators = [
            DataRequired()
        ]
            )
    productPrice = FloatField('ProductPrice',
        validators = [
            DataRequired()
        ]
    )
    submit=SubmitField('Add product!')

