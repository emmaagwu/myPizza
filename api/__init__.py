from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils import db
from .models.orders import Order
from .models.users import User

def create_app(config=config_dict['dev']):
  app=Flask(__name__)

  app.config.from_object(config)

  api=Api(app)

  api.add_namespace(order_namespace)
  api.add_namespace(auth_namespace)

  return app
