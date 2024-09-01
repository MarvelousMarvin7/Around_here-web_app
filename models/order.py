#!/usr/bin/python
""" holds class Order"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, String, Integer, Enum
from sqlalchemy.orm import relationship

class Order(BaseModel, Base):
    """Representation of Order """
    if models.storage_t == 'db':
        __tablename__ = 'orders'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        order_amount = Column(Integer, nullable=False, default=0)
        address = Column(String(128), nullable=False)
        payment_method = Column(Enum('cash', 'mobile_money'), nullable=False)
        status = Column(Enum('pending', 'processing', 'shipped', 'delivered', 'cancelled'), nullable=False, default='pending')
        order_items = relationship("OrderItem", backref="order")
    else:
        user_id = ""
        order_amount = 0
        address = ""
        payment_method = "mobile_money"
        status = "pending"

    def calculate_order_amount(self):
        """Calculates the total amount for the entire order."""
        self.order_amount = sum(item.total_amount for item in self.order_items)
        return self.order_amount

    def __init__(self, *args, **kwargs):
        """initializes Order"""
        super().__init__(*args, **kwargs)
