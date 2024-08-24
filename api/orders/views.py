from flask_restx import Namespace,Resource

order_namespace= Namespace('orders',description='a namespace for orders')

@order_namespace.route('/orders/')
class OrderGetCreate(Resource):

  def get(self):
    """
      Get all orders
    """
    pass

  def post(self):
    """
      Place a new order
    """
    pass

@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):

  def get(self,order_id):
    """
      Retrieve an order id
    """
    pass
  
  def put(self,order_id):
    """
      Update an order by order_id
    """
    pass

  def delete(self,order_id):
    """
      Delete an order by order_id
    """
    pass

@order_namespace.route('/user/<int:user_id>/order/<int:order_id>')
class GetUpdateDeleteForUser(Resource):

  def get(self,user_id, order_id):
    """
      Get user's specific order
    """
    pass

@order_namespace.route('/user/<int:user_id>/orders')
class GetUserOrders(Resource):

  def get(self, user_id):
    """
      Get all orders for a specific user
    """
    pass

@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):

  def patch(self,order_id):
    """
      Update order status by order_id
    """
    pass
