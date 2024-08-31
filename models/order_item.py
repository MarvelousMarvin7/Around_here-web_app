#!/usr/bin/python
""" holds class OrderItem"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Integer, event, Enum
from sqlalchemy.orm import relationship

class OrderItem(BaseModel, Base):
    """Representation of OrderItem """
    if models.storage_t == 'db':
        __tablename__ = 'order_items'
        order_id = Column(String(60), ForeignKey('orders.id'), nullable=False)
        product_id = Column(String(60), ForeignKey('products.id'), nullable=False)
        quantity = Column(Integer, nullable=False, default=0)
        unit_price = Column(Integer, nullable=False, default=0)
        total_amount = Column(Integer, nullable=False, default=0)
    else:
        order_id = ""
        product_id = ""
        quantity = ""
        unit_price = ""
        total_amount = ""

    def __init__(self, *args, **kwargs):
        """initializes OrderItem"""
        super().__init__(*args, **kwargs)
        self.get_total_amount()

    def get_total_amount(self):
        """calculates total amount"""
        self.total_amount = self.quantity * self.unit_price
        return self.total_amount

"""Event listener to automatically update order_amount in Order when OrderItem changes"""
@event.listens_for(OrderItem, 'after_insert')
@event.listens_for(OrderItem, 'after_update')
@event.listens_for(OrderItem, 'after_delete')
def update_order_amount(mapper, connection, target):
    """Event listener to update order_amount when OrderItem changes."""
    order = target.order
    if order is not None:
        order.calculate_order_amount()
        models.storage.save(order)
