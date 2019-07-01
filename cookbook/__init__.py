from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '0987ads0f987asd0987a0s9d8fa0s98d'
#  we use sqlite for development but we use postgresql for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from cookbook import routes