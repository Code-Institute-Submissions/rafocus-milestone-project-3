from datetime import datetime
from cookbook import db, login_manager
from flask_login import UserMixin # provides attributes required to manage session

# manages the sessions by loading the current user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    recipes = db.relationship('Recipe', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False, default='')
    ingredients = db.Column(db.Text, nullable=False, default='')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False, default='')
    preparation = db.Column(db.Text, nullable=False, default='')
    picture = db.Column(db.String(300), nullable=False, default='https://dummyimage.com/200')
    requirement = db.Column(db.String(150), nullable=False, default='')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # foreign key to the author of the recipe

    def __repr__(self):
        return f"Recipe('{self.title}', '{self.date}')"