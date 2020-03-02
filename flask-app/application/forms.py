from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Categories, Products

class AddCategory(FlaskForm):
    categoryName = StringField('CategoryName',
        validators = [
            DataRequired()
        ]
    )
class AddProduct(FlaskForm):
    productName = StringField('ProductName',
        validators = [
            DataRequired()
        ]
    )
    productInfo = StringField('ProductInfo',
        validators = [
            DataRequired()
        ]
    )
    productIMG = LargeBinaryField('ProductIMG',
        validators = [
            DataRequired()
        ]
            )
    productPrice = FloatField('ProductPrice',
        validators = [
            DataRequired()
        ]
    )

