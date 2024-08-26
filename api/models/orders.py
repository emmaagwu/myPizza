from ..utils.db import db
from enum import Enum


class Size(Enum):
  SMALL ='small'
  MEDIUM ='medium'
  LARGE ='large'
  EXTRA_LARGE ='extra_large'


class OrderStatus(Enum):
  PENDING='pending'
  IN_TRANSIT ='in_transit'
  DELIVERED ='delivered'


class Order(db.Model):
  __tablename__ = 'orders'
  id=db.Column(db.Integer(), primary_key=True)
  size=db.Column(db.Enum(Size), default=Size.SMALL)
  order_status=db.Column(db.Enum(OrderStatus),default=OrderStatus.PENDING)
  flavour=db.Column(db.String(), nullable=False)
  quantity=db.Column(db.Integer())
  user=db.Column(db.Integer(),db.ForeignKey('users.id'))

  def __rep__(self):
    return f"<Order {self.id}>"

  

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_by_id(cls, id):
    return cls.query.get_or_404(id)