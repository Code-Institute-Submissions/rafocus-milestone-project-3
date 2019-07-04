import os
from flask import Flask, render_template, url_for, flash, redirect, request, abort
from cookbook import app, db, bcrypt
from cookbook.forms import RegisterForm, LoginForm, RecipeForm
from cookbook.models import User, Recipe
from flask_login import login_user, current_user, logout_user, login_required



# routes

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int) # 1 the initial value
    recipes = Recipe.query.order_by(Recipe.date.desc()).paginate(page=page, per_page=5) #recent first, 9 per page
    return render_template('home.html', recipes=recipes)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm() # create an instance of the form and pass it on to the template as a variable with 'form=form'
    if form.validate_on_submit():
        hashpass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashpass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success') # sending a message to the next request
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

@app.route("/myaccount")
@login_required # decorator to restrict access to this route
def myaccount():
    return render_template('my_account.html')

@app.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data, description=form.description.data, picture=form.picture.data, method=form.method.data, author=current_user)
        db.session.add(recipe)
        db.session.commit()
        flash('New Recipe Created', 'success')
        return redirect(url_for('home'))
    return render_template('new_recipe.html', form=form)

@app.route("/recipe/<int:recipe_id>")
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', recipe=recipe)

@app.route("/recipe/<int:recipe_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        return abort(403)
    form = RecipeForm()    
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.method = form.method.data
        recipe.picture = form.picture.data
        db.session.commit()
        flash('Recipe updated', 'success')
        return redirect(url_for('recipe', recipe_id=recipe.id))
    elif request.method == 'GET':
        form.title.data = recipe.title
        form.description.data = recipe.description
        form.method.data = recipe.method
        form.picture.data = recipe.picture
    return render_template('new_recipe.html', form=form)

@app.route("/recipe/<int:recipe_id>/delete", methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        return abort(403)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted', 'success')
    return redirect(url_for('home'))
