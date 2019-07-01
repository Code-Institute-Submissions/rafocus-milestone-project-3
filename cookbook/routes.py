from flask import Flask, render_template, url_for, flash, redirect
from cookbook import app, db, bcrypt
from cookbook.forms import RegisterForm, LoginForm
from cookbook.models import User, Recipe
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashpass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashpass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')) # if the user is already authenticated it will be redirected to home
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): #check if password enetered in the form is same as in the database
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Please check your login credentials', 'danger')
    return render_template('login.html', form=form)

# if the user is logged out it will be redirected to home
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))