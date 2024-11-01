from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy() 
DB_NAME = "youtube_management"


def create_app(): 
    app = Flask(__name__)  
    app.config['SECRET_KEY'] = "nigganigga"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:AchSQL2024#@localhost/youtube_management" 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    from .views import views 
    from .auth import auth

    app.register_blueprint(views , url_prefix = '/') 
    app.register_blueprint(auth, url_prefix = '/')

    return app