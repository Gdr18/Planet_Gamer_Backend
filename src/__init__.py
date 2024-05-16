from flask import Flask
from flask_cors import CORS

from .database.db import db, bcrypt

from .routes.address_route import address
from .routes.basket_route import basket
from .routes.user_route import user
from .routes.game_route import game
from .routes.role_route import role
from .routes.order_route import order
from .services.auth_service import auth
# from .models.role_model import Role
# from .models.user_model import User


app = Flask(__name__)

cors = CORS()


def create_app(config):
    app.config.from_object(config)

    db.init_app(app)
    cors.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(user)
    app.register_blueprint(order)
    app.register_blueprint(address)
    app.register_blueprint(basket)
    app.register_blueprint(game)
    app.register_blueprint(role)
    app.register_blueprint(auth)

    with app.app_context():
        # Role.__table__.drop(bind=db.engine)
        # User.__table__.drop(bind=db.engine)
        db.create_all()

    return app
