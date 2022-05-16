from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(),Email()])
    username = StringField('Your username',validators=[Required()])
    password = PasswordField('password', validators=[Required(),EqualTo('password_confirm',message='Password must match')])
    password_confirm = PasswordField('confirm passowrd', validators=[Required()])
    submit = SubmitField('Sign up')
    
    def validate_email(self,data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Theres an account with that email')
        
    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('The username  has already been taken')
    
class LoginForm(FlaskForm):
    email = StringField('Your email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit   = SubmitField('Sign In')
    