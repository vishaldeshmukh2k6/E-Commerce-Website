from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS


db = SQLAlchemy()
DB_NAME = "database.sqlite3"

def create_database():
    db.create_all()
    print('Database Created!')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'vishal deshmukh'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    CORS(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


    @login_manager.user_loader
    def load_user(id):
        return Customer.query.get(int(id))
    

    from .views import views
    from .auth import auth
    from .admin import admin
    from .api import api
    from .models import Customer, Product, Order, Cart, Category, Address, Review, Wishlist, OrderItem 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')

    with app.app_context(): 
        create_database()


    return app


