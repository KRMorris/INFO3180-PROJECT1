from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = ' key secret super'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://info3180proj1:info3180@localhost:5433/info3180"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/info3180"
db=SQLAlchemy(app)

app.config.from_object(__name__)

from app import views,model
