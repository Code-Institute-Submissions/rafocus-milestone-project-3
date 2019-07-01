from flask import Flask, render_template, url_for, flash, redirect
from cookbook import app
from cookbook.forms import RegisterForm, LoginForm
from cookbook.models import User, Recipe


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
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@email.com' and form.password.data == 'password':
            flash('Logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check your login credentials', 'danger')
    return render_template('login.html', form=form)