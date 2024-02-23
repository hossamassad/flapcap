from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from vending.config import Config
from vending.models.Coinstack import Coinstack

bcrypt = Bcrypt()
db = SQLAlchemy(session_options={'expire_on_commit': False})
login_manager = LoginManager()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from vending.api.main_page import main_page
    from vending.api.product_api import product
    from vending.api.user_api import users
    app.register_blueprint(main_page)
    app.register_blueprint(product, url_prefix='/product')
    app.register_blueprint(users, url_prefix='/user')

    with app.app_context():
        bcrypt.init_app(app)
        db.init_app(app)
        db.create_all()
        login_manager.init_app(app)

    with app.app_context():
        coinstack = Coinstack.query.get(1)
        if coinstack is None:
            coinstack = Coinstack()
            db.session.add(coinstack)
            db.session.commit()

    return app
