from flask_restx import Namespace,Resource

auth_namespace = Namespace('auth', description='a namespace for authentication')

@auth_namespace.route('/signup')
class SignUp(Resource):

  def post(self):
    """
      Create a new user
    """
    pass

@auth_namespace.route('/login')
class Login(Resource):

  def post(self):
    """
      Generate a JWT pair
    """
    pass
