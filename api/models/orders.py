from ..utils import db
from enum import Enum
from datetime import datetime

class Sizes:
  SMALL ='small'
  MEDIUM ='medium'
  LARGE ='large'
  EXTRA_LARGE ='extra_large'


class OrderStatus:
  PENDING='pending'
  IN_TRANSIT ='in_transit'
  DELIVERED ='delivered'


class Order(db.Model):
  __tablename__ = 'orders'
  id=db.Column(db.Integer(), primary_key=True)
  size=db.column(db.Enum(Sizes),default=Sizes.SMALL)
  order_status=db.column(db.Enum(OrderStatus),default=OrderStatus.PENDING)
  flavor=db.column(db.String(), nullable=False)
  date_created=db.column(db.DateTime(),default=datetime.utc)
  user=db.Column(db.Integer(),db.ForeignKey('users.id'), nullable=False)

  def __rep__(self):
    return f"<Order {self.id}>"

  

  def __repr__(self):
    return f"<User {self.username}>"
