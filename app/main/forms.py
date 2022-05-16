from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,TextAreaField)
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio =TextAreaField('Tell us about yourself', validators=[])
    submit = SubmitField('Submit')    
    
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('product', 'product'), ('idea', 'idea'), ('business', 'business')],
                           validators=[Required()])
    submit = SubmitField('Post blog')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')


class Vote(FlaskForm):
    submit = SelectField('Like')
