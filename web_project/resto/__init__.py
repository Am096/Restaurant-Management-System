
#from resto import app
#from resto import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SECRET_KEY'] = '7911449938800f82bc6a03af'
db = SQLAlchemy(app)

from resto import routes

