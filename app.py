from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from blueprints import bp

from models import user as u
from config import Config
from models import db



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return u.User.query.get(int(user_id)) 

app.register_blueprint(bp)



