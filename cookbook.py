from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = '0987ads0f987asd0987a0s9d8fa0s98d'

recipes = [
    {
        'name': 'recipe 1',
        'description': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sapiente, rem?',
        'method': ['step1', 'step 2', 'step 3'],
        'picture': 'https://dummyimage.com/300' 
    },
    {
        'name': 'recipe 2',
        'description': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sapiente, rem?',
        'method': ['step1', 'step 2', 'step 3'],
        'picture': 'https://dummyimage.com/300' 
    }
]

# routes

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', recipes=recipes)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

# registration form fields
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# login form fields
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

if __name__ == '__main__':
    app.run(debug=True)