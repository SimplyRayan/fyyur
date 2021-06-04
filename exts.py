from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask import Flask

print(__name__)
app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)

migrate = Migrate(app,db)

