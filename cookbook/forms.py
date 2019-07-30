from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cookbook.models import User

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

# registration form fields
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists')

# login form fields
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    cuisine = SelectField('Cuisine', choices=[('1','Mediterranean'), ('2','European'), ('3','Asian')])
    requirement = StringField('Allergy')
    picture = StringField('Picture URL')
    description = TextAreaField('Description')
    ingredients = TextAreaField('Ingredients')
    preparation = TextAreaField('Method')
    submit = SubmitField('Create')

class SearchForm(FlaskForm):
    searchString = StringField('Search expression', validators=[DataRequired()])
    searchField = SelectField('Search in:', choices=[('title','Title'), ('description','Description'), ('ingredients','Ingredients'), ('preparation','Method'), ('requirement','Allergy')])
    submit = SubmitField('Search')

