from flask_restx import Namespace,Resource,fields
from flask import request
from ..models.users import User
from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (create_access_token,create_refresh_token,
                                jwt_required,get_jwt_identity,)
from werkzeug.exceptions import Conflict,BadRequest

auth_namespace = Namespace('auth', description='a namespace for authentication')


signup_model=auth_namespace.model(
  'SignUp', {
    'id':fields.Integer(),
    'username':fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'password': fields.String(required=True, description='The password of the user'),
  }
)

user_model=auth_namespace.model(
  'User', {
    'id':fields.Integer(),
    'username':fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'password_hash': fields.String(required=True, description='The password of the user'),
    'is_active': fields.Boolean(description='This shows that User is active'),
    'is_staff': fields.Boolean(description='This shows that User is staff'),
  }
)

login_model=auth_namespace.model(
  'Login', {
    'email': fields.String(required=True, description='The email of the user'),
    'password': fields.String(required=True, description='The password of the user'),
  }
)

@auth_namespace.route('/signup')
class SignUp(Resource):

  @auth_namespace.expect(signup_model)
  @auth_namespace.marshal_with(user_model)
  def post(self):
    """
      Create a new user
    """
    data = request.get_json()

    try:

      new_user=User(
        username=data.get('username'),
        email=data.get('email'),
        password_hash=generate_password_hash(data.get('password')) # TODO: hash password
      )


      new_user.save()

      return new_user, HTTPStatus.CREATED

    except Exception:
      raise Conflict(f"User with email {data.get('email')} already exists") from None

@auth_namespace.route('/login')
class Login(Resource):

  @auth_namespace.expect(login_model)
  def post(self):
    """
      Generate a JWT pair
    """

    data = request.get_json()

    email=data.get('email')
    password=data.get('password')

    user = User.query.filter_by(email=email).first()

    if user is not None and check_password_hash(user.password_hash,password):
      access_token=create_access_token(identity=user.username)
      refresh_token=create_refresh_token(identity=user.username)
      response={
        'access_token':access_token,
        'refresh_token':refresh_token
      }      

      return response, HTTPStatus.OK
    
    raise BadRequest("Invalid Username or password")

@auth_namespace.route('/refresh')
class Refresh(Resource):
  @jwt_required(refresh=True)
  def post(self):
    username=get_jwt_identity()

    access_token=create_access_token(identity=username)

    return {'access_token':access_token}, HTTPStatus.OK
