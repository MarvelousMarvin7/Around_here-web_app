#!/usr/bin/python
""" holds class OrderItem"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, ForeignKey, Float, String, Integer, event, Enum
from sqlalchemy.orm import relationship

class OrderItem(BaseModel, Base):
    """Representation of OrderItem """
    if models.storage_t == 'db':
        __tablename__ = 'order_items'
        order_id = Column(String(60), ForeignKey('orders.id'), nullable=False)
        product_id = Column(String(60), ForeignKey('products.id'),
                             nullable=False)
        quantity = Column(Integer, nullable=False, default=0)
        unit_price = Column(Float, nullable=False, default=0.00)
        total_amount = Column(Float, nullable=False, default=0.00)
    else:
        order_id = ""
        product_id = ""
        quantity = ""
        unit_price = ""
        total_amount = ""

    def calculate_total_amount(self):
        """calculates total amount"""
        self.total_amount = self.quantity * self.unit_price
        return self.total_amount

    def __init__(self, *args, **kwargs):
        """initializes OrderItem"""
        super().__init__(*args, **kwargs)
        self.calculate_total_amount()
